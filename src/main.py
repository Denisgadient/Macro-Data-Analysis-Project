import argparse
import pandas as pd
import os
import yfinance as yf
import numpy as np
import statsmodels.api as sm

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ticker", default="^GSPC")
    parser.add_argument("--events", default="data/events.csv")
    args = parser.parse_args()

    os.makedirs("output/plots", exist_ok=True)
    os.makedirs("output/reports", exist_ok=True)

    # 1. Fetch Market Data
    df = yf.download(args.ticker, start="2023-01-01", auto_adjust=True)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    # 2. Compute Ex-Ante Volatility (No Lookahead Bias)
    returns = df['Close'].pct_change()
    vol_60_ex_ante = returns.shift(1).rolling(60).std()

    # 3. Process Events with Deterministic Alignment
    events = pd.read_csv(args.events)
    events['date'] = pd.to_datetime(events['date']).dt.tz_localize(None)
    
    results = []
    for _, row in events.iterrows():
        # Searchsorted finds exact or next trading day (deterministic)
        pos = df.index.searchsorted(row['date'])
        if pos >= len(df.index) or pos < 60: continue
        
        vol_pre = vol_60_ex_ante.iloc[pos]
        if np.isnan(vol_pre): continue

        # Calculate Z-m1_p1 (2-day window scaled by sqrt(2))
        r_m1_p1 = (df['Close'].iloc[pos+1] / df['Close'].iloc[pos-1]) - 1
        surprise_z = (row['actual'] - row['consensus']) / row['std_dev_hist']
        
        results.append({
            'event_id': row['event_id'],
            'event_type': row['event_type'],
            'z_m1_p1': r_m1_p1 / (vol_pre * np.sqrt(2)),
            'surprise_z': surprise_z
        })

    res_df = pd.DataFrame(results)
    res_df.to_csv("output/processed_impacts.csv", index=False)

    # 4. Institutional Stats (Robust OLS)
    X = sm.add_constant(res_df['surprise_z'])
    model = sm.OLS(res_df['z_m1_p1'], X).fit(cov_type='HC1')
    
    print("\n--- INSTITUTIONAL DESK SUMMARY ---")
    print(f"BETA: {model.params['surprise_z']:.4f}")
    print(f"T-STAT: {model.tvalues['surprise_z']:.4f}")
    print(f"P-VALUE: {model.pvalues['surprise_z']:.4f}")
    print(f"R2: {model.rsquared:.4f}")
    print(f"N: {int(model.nobs)}")

if __name__ == "__main__":
    main()
