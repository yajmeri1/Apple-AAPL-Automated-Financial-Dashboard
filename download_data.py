import yfinance as yf
import pandas as pd
from pathlib import Path

# Get the project root folder
project_root = Path(__file__).resolve().parents[1]

# Create excel folder if it does not exist
excel_folder = project_root / "excel"
excel_folder.mkdir(exist_ok=True)

# Download Apple data
apple = yf.Ticker("AAPL")

income = apple.financials.transpose()
balance = apple.balance_sheet.transpose()
cashflow = apple.cashflow.transpose()

# Save files
income.to_excel(excel_folder / "income.xlsx")
balance.to_excel(excel_folder / "balance.xlsx")
cashflow.to_excel(excel_folder / "cashflow.xlsx")

print("Apple data downloaded successfully")

# -----------------------------
# Create summary metrics
# -----------------------------

# Ensure chronological order
income = income.sort_index()
cashflow = cashflow.sort_index()

# Convert all values to numeric
income = income.apply(pd.to_numeric, errors='coerce')
cashflow = cashflow.apply(pd.to_numeric, errors='coerce')

# --- Identify revenue column robustly ---
revenue_keywords = ["total revenue", "revenue", "revenues"]

revenue_col = next(
    (c for c in income.columns if any(k in str(c).lower() for k in revenue_keywords)),
    None
)

if revenue_col is None:
    raise ValueError(f"Could not find revenue column. Columns: {income.columns.tolist()}")

revenue = income[revenue_col].dropna()

# --- Identify or calculate Free Cash Flow robustly ---
fcf_keywords = ["free cash flow", "fcf"]

fcf_col = next(
    (c for c in cashflow.columns if any(k in str(c).lower() for k in fcf_keywords)),
    None
)

if fcf_col:
    free_cash_flow = cashflow[fcf_col].dropna()
else:
    # Find CFO and CapEx
    cfo_col = next((c for c in cashflow.columns if "operat" in str(c).lower()), None)
    capex_col = next((c for c in cashflow.columns if "capex" in str(c).lower() or "capital" in str(c).lower()), None)

    if cfo_col is None or capex_col is None:
        raise ValueError(f"Cannot find CFO or CapEx. Columns: {cashflow.columns.tolist()}")

    free_cash_flow = (cashflow[cfo_col] - cashflow[capex_col]).dropna()

# --- Align indexes ---
revenue, free_cash_flow = revenue.align(free_cash_flow, join="inner")

# Safety check
if len(revenue) < 2 or len(free_cash_flow) < 2:
    raise ValueError("Not enough data to compute CAGR. Check downloaded financials.")

# --- Calculate metrics ---
revenue_cagr = (revenue.iloc[-1] / revenue.iloc[0]) ** (1 / (len(revenue) - 1)) - 1
fcf_cagr = (free_cash_flow.iloc[-1] / free_cash_flow.iloc[0]) ** (1 / (len(free_cash_flow) - 1)) - 1
average_fcf_margin = (free_cash_flow / revenue).mean()

# --- Create metrics table ---
summary_df = pd.DataFrame({
    "Metric": [
        "Revenue CAGR",
        "Free Cash Flow CAGR",
        "Average Free Cash Flow Margin"
    ],
    "Value": [
        revenue_cagr,
        fcf_cagr,
        average_fcf_margin
    ]
})

# --- Save metrics ---
import matplotlib.pyplot as plt

# Create charts folder
charts_folder = project_root / "charts"
charts_folder.mkdir(exist_ok=True)

# Revenue over time
revenue.plot(title="AAPL Revenue Over Time")
plt.ylabel("Revenue ($)")
plt.savefig(charts_folder / "revenue_over_time.png")
plt.close()

# Free Cash Flow over time
free_cash_flow.plot(title="AAPL Free Cash Flow Over Time")
plt.ylabel("FCF ($)")
plt.savefig(charts_folder / "fcf_over_time.png")
plt.close()

summary_df.to_excel(excel_folder / "summary_metrics.xlsx", index=False)
print("Summary metrics updated successfully")


