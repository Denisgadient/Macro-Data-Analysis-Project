# Macro Event Impact Lab

A quantitative framework to measure S&P 500 sensitivity to US macroeconomic surprises (CPI & NFP).

## Features
- **Surprise-Based Analysis:** Normalizes macro data into standard deviation "Sigmas."
- **Volatility Normalization:** Scales returns by 60-day rolling realized volatility for regime-agnostic comparison.
- **Statistical Rigor:** Calculates Event Betas, R-Squared, and P-Values via OLS regression.

## Project Structure
- `data/`: Raw event timestamps and consensus data.
- `src/`: Data loading, statistical engine, and report generation logic.
- `output/`: Generated research notes and sensitivity plots.

## Quick Start
Run `python src/data_loader.py` followed by `python src/stats_engine.py` to generate the latest impact metrics.
