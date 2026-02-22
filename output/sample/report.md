# Macroeconomic Event Impact Analysis: S&P 500 (2024)

## Executive Summary
This study analyzes the S&P 500 sensitivity to US CPI and NFP surprises using an institutional-grade event study framework. 

- **Sample Size (N):** 15
- **Event Types:** CPI, NFP
- **Primary Window:** T-1 to T+1 (Relative to Close)

## Methodology (Institutional Spec)
1. **Aligning Dates:** I made sure the macro release dates matched the actual market trading days. If data came out on a Sunday, the code looks at the market move on Monday.
2. **Volatility Adjustment:** To make sure quiet days and volatile days are treated fairly, I scaled the returns using a 60-day rolling average. This prevents one "crazy" day from ruining the whole model.
3. **Window Scaling:** Multi-day windows (e.g., T-1 to T+1) are scaled by sqrt(T) to maintain Z-score consistency.
4. **Cleaning the Data:** I used a standard statistical correction (HC1) to handle the "noise" typically found in stock market price changes.

## Key Findings
- **Market Reaction:** The negative beta shows that "better than expected" data actually caused the market to fall. In 2024, investors were more worried about high interest rates than they were happy about a strong economy.
- **Pre-Event Moves:** I looked at the days before the news broke to see if the market was already "leaking" the move, which helps show how much of the news was truly a surprise.

## Limitations
- **Daily vs. Intraday:** This uses daily closing prices. Using minute-by-minute data would be more precise for the exact moment of the news release, but daily data shows the lasting impact of the day.
- **Sample Constraints:** These results are specific to 2024. If we were in a different year with lower interest rates, the market might react completely differently to "good" news.
