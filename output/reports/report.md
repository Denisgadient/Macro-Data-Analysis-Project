# Institutional Macro Impact Report (v2.0)

## Executive Summary
This study analyzes the S&P 500 sensitivity to US CPI and NFP surprises using an institutional-grade event study framework. 

- **Sample Size (N):** 15
- **Event Types:** CPI, NFP
- **Primary Window:** T-1 to T+1 (Relative to Close)

## Methodology (Institutional Spec)
1. **Deterministic Alignment:** T0 is defined as the release date if it is a trading day, otherwise the next available trading day.
2. **Ex-Ante Vol Normalization:** Returns are scaled by 60-day realized volatility calculated up to T-1 to avoid lookahead bias.
3. **Window Scaling:** Multi-day windows (e.g., T-1 to T+1) are scaled by sqrt(T) to maintain Z-score consistency.
4. **Robust Statistics:** Regressions utilize HC1 Robust Standard Errors to account for heteroscedasticity in financial returns.

## Key Findings
- **Directionality:** The negative beta suggests that macro surprises (data exceeding consensus) tended to result in negative price action during this period.
- **Leakage Diagnostic:** Average Z-score for pre-event windows is being monitored for potential information asymmetry.

## Limitations
- **Proxy Data:** Analysis uses daily close data; intraday high-frequency data would provide more granular reaction metrics.
- **Sample Constraints:** 2024 represents a specific interest rate regime; results may differ in low-rate environments.
