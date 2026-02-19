import pandas as pd
from scipy import stats
import datetime

def generate_markdown():
    df = pd.read_csv('output/processed_impacts.csv')
    slope, intercept, r_value, p_value, std_err = stats.linregress(df['surprise'], df['vol_adj_return'])
    
    report_content = f"""# Macro Event Impact Analysis Report
Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}

## Executive Summary
This analysis quantifies the sensitivity of the S&P 500 (^GSPC) to US Macroeconomic surprises (CPI & NFP) during the 2024 period.

## Statistical Significance
| Metric | Value | Interpretation |
| :--- | :--- | :--- |
| **Event Beta** | {slope:.4f} | Units of volatility move per 1-sigma surprise |
| **R-Squared** | {r_value**2:.4f} | % of variance explained by macro surprise |
| **P-Value** | {p_value:.4f} | Statistical significance (Target < 0.05) |

## Visual Analysis
![Event Sensitivity Plot](plots/event_sensitivity.png)

## Methodology
- **Surprise Calculation:** (Actual - Consensus) / Historical Std Dev.
- **Volatility Normalization:** Returns scaled by 60-day rolling realized volatility.
- **Window:** T-1 to T+1 relative to event timestamp.
"""
    
    with open('output/reports/README_RESULTS.md', 'w') as f:
        f.write(report_content)
    
    print("\nSuccess: Professional Markdown report generated in output/reports/README_RESULTS.md")

if __name__ == "__main__":
    generate_markdown()
