# Macro Event Impact Analysis Report
Generated on: 2026-02-19 19:50

## Executive Summary
This analysis quantifies the sensitivity of the S&P 500 (^GSPC) to US Macroeconomic surprises (CPI & NFP) during the 2024 period.

## Statistical Significance
| Metric | Value | Interpretation |
| :--- | :--- | :--- |
| **Event Beta** | -0.3091 | Units of volatility move per 1-sigma surprise |
| **R-Squared** | 0.0988 | % of variance explained by macro surprise |
| **P-Value** | 0.2538 | Statistical significance (Target < 0.05) |

## Visual Analysis
![Event Sensitivity Plot](plots/event_sensitivity.png)

## Methodology
- **Surprise Calculation:** (Actual - Consensus) / Historical Std Dev.
- **Volatility Normalization:** Returns scaled by 60-day rolling realized volatility.
- **Window:** T-1 to T+1 relative to event timestamp.
