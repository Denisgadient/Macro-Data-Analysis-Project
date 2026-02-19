# Macro Event Impact Lab (Institutional Grade)

A quantitative framework to measure S&P 500 sensitivity to US macroeconomic surprises using ex-ante volatility normalization and robust OLS regression.

## Key Findings
- **Event Beta:** Measures the units of market volatility move per 1-sigma surprise in CPI/NFP.
- **Interpretation:** A beta of -0.22 means a 1-standard deviation "beat" in macro data historically correlates with a 0.22 sigma drop in the S&P 500.
- **Outputs:** All statistical results and distribution plots are stored in the `output/` directory.

## Methodology (Academic Standards)
- **Ex-Ante Volatility:** Returns are scaled by 60-day rolling realized volatility calculated at T-1 to eliminate lookahead bias.
- **Deterministic Alignment:** Event dates are mapped to the next available trading day using searchsorted logic.
- **Statistical Rigor:** Regression analysis utilizes HC1 Robust Standard Errors to account for heteroscedasticity.

## Quick Start
Run the full pipeline with a single command:
```bash
python -m src.main --ticker ^GSPC --events data/events.csv
```

## Project Structure
- `src/main.py`: Primary entry point for data fetching and OLS modeling.
- `src/distribution_plot.py`: Visualizes return distributions split by event type (CPI vs NFP).
- `output/reports/report.md`: Auto-generated executive summary.
