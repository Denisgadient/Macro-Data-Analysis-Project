# Macro Sensitivity Analysis: S&P 500

This project investigates how major US economic releases—specifically CPI and Non-Farm Payrolls (NFP) impact the daily returns of the S&P 500. By comparing actual data against analyst consensus, I've quantified the "Event Beta" to see how the market reacts to economic surprises.

## Key Findings
- **Event Beta:** Measures the market move (in volatility units) per 1-standard deviation surprise.
- **Finding:** A negative beta (~ -0.31) indicates that in 2024, "stronger" data releases typically led to market sell-offs.
- **Outputs:** All statistical results and distribution plots are stored in the `output/` directory.

## Statistical Approach
- **Volatility Normalization:** Returns are scaled by a 60-day rolling realized volatility. This ensures moves are measured relative to the specific market environment.
- **Regression Model:** Used OLS regression with HC1 Robust Standard Errors to account for the inherent noise in financial data.

## Quick Start
Run the full pipeline with a single command:
```bash
python -m src.main --ticker ^GSPC --events data/events.csv
```

## Project Layout
- `/data`: S&P 500 prices and macro event history.
- `src`: Python scripts for data processing and OLS modeling.
- `output`: Statistical reports and return distribution plots.
