import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_plots():
    df = pd.read_csv('output/processed_impacts.csv')
    os.makedirs('output/plots', exist_ok=True)
    
    # Histogram of moves split by event type
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x='z_m1_p1', hue='event_type', kde=True, bins=15)
    
    plt.title('Distribution of Vol-Adjusted Returns by Event Type', fontsize=14)
    plt.xlabel('Vol-Adjusted Return (Z-Score)', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.axvline(0, color='black', linestyle='--')
    
    plt.savefig('output/plots/distribution_plot.png')
    print("\nSuccess: Distribution plot saved to output/plots/distribution_plot.png")

if __name__ == "__main__":
    generate_plots()
