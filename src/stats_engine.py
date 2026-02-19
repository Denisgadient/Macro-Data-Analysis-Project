import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import os

def run_analysis():
    # Load the data we just generated
    df = pd.read_csv('output/processed_impacts.csv')
    
    if len(df) < 2:
        print("Not enough data points for regression yet. Add more events to events.csv!")
        return

    # 1. Calculate Regression (The "Beta")
    # x = surprise, y = vol_adj_return
    slope, intercept, r_value, p_value, std_err = stats.linregress(df['surprise'], df['vol_adj_return'])
    
    print("\n--- STATISTICAL ANALYSIS RESULTS ---")
    print(f"Event Beta: {slope:.4f}")
    print(f"R-Squared:  {r_value**2:.4f}")
    print(f"P-Value:    {p_value:.4f}")
    
    # 2. Create the Visualization
    plt.figure(figsize=(10, 6))
    sns.regplot(data=df, x='surprise', y='vol_adj_return', 
                scatter_kws={'s': 100, 'alpha': 0.6}, 
                line_kws={'color': 'red', 'label': f'Beta: {slope:.2f}'})
    
    plt.title('Market Sensitivity to Macro Surprises', fontsize=14)
    plt.xlabel('Surprise (Standard Deviations)', fontsize=12)
    plt.ylabel('Market Move (Vol-Adjusted Return)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    
    # Save the chart
    os.makedirs('output/plots', exist_ok=True)
    plt.savefig('output/plots/event_sensitivity.png')
    print("\nSuccess: Chart saved to output/plots/event_sensitivity.png")

if __name__ == "__main__":
    run_analysis()
