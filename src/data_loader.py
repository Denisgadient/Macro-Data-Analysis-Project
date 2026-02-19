import pandas as pd
import yfinance as yf
import os
from datetime import timedelta

class MacroDataLoader:
    def __init__(self, events_path):
        self.events = pd.read_csv(events_path)
        self.cache_dir = "data/cache"
        os.makedirs(self.cache_dir, exist_ok=True)

    def get_market_data(self, ticker, start_date, end_date):
        cache_file = f"{self.cache_dir}/{ticker.replace('^', '')}.csv"
        # If a broken cache exists, remove it to start fresh
        if os.path.exists(cache_file):
            os.remove(cache_file)
            
        print(f"Fetching {ticker} from Yahoo Finance...")
        data = yf.download(ticker, start=start_date, end=end_date, auto_adjust=True)
        
        # CRITICAL FIX: Flatten MultiIndex columns
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.get_level_values(0)
            
        data.to_csv(cache_file)
        return data

    def process_impacts(self, market_ticker="^GSPC"):
        results = []
        self.events['date'] = pd.to_datetime(self.events['date'])
        start = (self.events['date'].min() - timedelta(days=100)).strftime('%Y-%m-%d')
        end = (self.events['date'].max() + timedelta(days=10)).strftime('%Y-%m-%d')
        
        market_data = self.get_market_data(market_ticker, start, end)
        
        # Ensure we are working with numeric data
        close_prices = pd.to_numeric(market_data['Close'], errors='coerce').dropna()
        returns = close_prices.pct_change()
        vol = returns.rolling(window=60).std()

        for _, event in self.events.iterrows():
            date = event['date']
            try:
                # Find the actual trading day
                target_idx = close_prices.index.get_indexer([date], method='nearest')[0]
                
                pre_event_price = close_prices.iloc[target_idx-1]
                post_event_price = close_prices.iloc[target_idx+1]
                real_vol = vol.iloc[target_idx]
                
                raw_return = (post_event_price / pre_event_price) - 1
                vol_adj_return = raw_return / real_vol
                surprise = (event['actual'] - event['consensus']) / event['std_dev_hist']
                
                results.append({
                    'event_id': event['event_id'],
                    'date': date.strftime('%Y-%m-%d'),
                    'surprise': round(float(surprise), 2),
                    'raw_return_%': round(float(raw_return * 100), 3),
                    'vol_adj_return': round(float(vol_adj_return), 3)
                })
            except Exception as e:
                print(f"Error processing {event['event_id']}: {e}")
                
        return pd.DataFrame(results)

if __name__ == "__main__":
    loader = MacroDataLoader("data/events.csv")
    impact_df = loader.process_impacts("^GSPC")
    print("\n--- INSTITUTIONAL EVENT ANALYSIS ---")
    print(impact_df.to_string(index=False))
    os.makedirs("output", exist_ok=True)
    impact_df.to_csv("output/processed_impacts.csv", index=False)
    print("\nSuccess: Results saved to output/processed_impacts.csv")
