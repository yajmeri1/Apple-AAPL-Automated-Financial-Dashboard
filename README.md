AAPL Financial Analysis & Forecasting Model
Project Overview
This repository contains a complete financial analysis and forecasting model for Apple Inc. (AAPL). It combines Python automation with a structured Excel workbook to analyze historical performance, calculate key financial metrics, and generate forward‑looking projections.
The project demonstrates practical skills in financial modeling, data cleaning, KPI development, visualization, and reproducible analytics.

Key Features
- Automated data cleaning and preprocessing using Python
- Historical financial analysis (Revenue, Free Cash Flow, Margins, EPS, etc.)
- CAGR calculations for key performance metrics
- KPI dashboard summarizing company performance
- Forecast model projecting future financials
- Matplotlib visualizations for trends and insights
- Organized Excel workbook containing all cleaned data, KPIs, and forecasts
- Dynamic Excel dashboard using XLOOKUP to compare Free Cash Flow vs Revenue across selected years

Project Structure
AAPL-Financial-Analysis-Forecasting-Model/
│
├── scripts/               # Python scripts for cleaning, metrics, charts
│   ├── analysis.py
│   ├── metrics.py
│   ├── charts.py
│   └── clean_data.py
│
├── data/                  # Excel model with all financials
│   └── AAPL_Financial_Model.xlsx
│
├── charts/                # Exported PNG charts
│   ├── revenue_chart.png
│   └── fcf_chart.png
│
└── README.md              # Project documentation



Python Components
The Python scripts handle:
- Data cleaning and formatting
- Error‑handled metric calculations
- CAGR functions
- Automated chart generation
- Export of cleaned datasets and visuals
This ensures the workflow is reproducible and scalable.

Excel Model
The Excel workbook includes:
- Cleaned historical financial statements
- KPI summary
- Forecast model
- Visual dashboard
- A dynamic comparison tool using XLOOKUP to pull Revenue and Free Cash Flow values based on user‑selected years
This allows the dashboard to update automatically when the user changes the selected period.

How to Run the Python Scripts
Install required libraries:
pip install pandas numpy matplotlib openpyxl


Run the analysis:
python analysis.py


Charts and updated Excel outputs will be saved automatically.

Future Improvements
- Add a full DCF valuation
- Integrate API‑based data pulls
- Build a Streamlit dashboard
- Add sensitivity analysis
- Automate Excel export formatting
