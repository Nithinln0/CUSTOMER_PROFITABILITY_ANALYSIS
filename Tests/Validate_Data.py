import pandas as pd
import numpy as np

# --- Configuration ---
# NOTE: Replace 'path/to/your/clean_data.csv' with the actual path to your source file
FILE_PATH = 'C:/CustomerProfitabilityProject/Data/cleaned_cdr.csv'
TOTAL_REVENUE_COLUMN = 'Total_Revenue'
COST_COLUMN = 'Acquisition_Cost'
CUSTOMER_ID_COLUMN = 'Customer_ID'
MONTH_COLUMN = 'Month'

print("--- Starting Power BI Data Validation Tests ---")

try:
    # 1. Load Data
    df = pd.read_csv(FILE_PATH)
    print(f"✅ Data Loaded successfully. Total Rows: {len(df)}")

    # 2. Data Quality Check: Missing Values
    missing_count = df.isnull().sum().sum()
    if missing_count == 0:
        print("✅ Data Quality Test: No missing values found across all columns.")
    else:
        print(f"⚠️ Data Quality Warning: Found {missing_count} total missing values.")
        
    # 3. Data Quality Check: Duplicates
    duplicate_rows = df.duplicated().sum()
    if duplicate_rows == 0:
        print("✅ Data Quality Test: No duplicate rows found.")
    else:
        print(f"❌ Data Quality Failure: Found {duplicate_rows} duplicate rows.")

    # 4. KPI Validation: Total Revenue
    # Match this against your Power BI Card visual for Total Revenue
    total_revenue_calc = df[TOTAL_REVENUE_COLUMN].sum()
    print(f"\n✨ Validating Core KPIs:")
    print(f"  - Calculated Total Revenue: ₹{total_revenue_calc:,.2f}")

    # 5. KPI Validation: Unique Customers
    # Match this against your Power BI Card visual for Customers
    unique_customers_calc = df[CUSTOMER_ID_COLUMN].nunique()
    print(f"  - Calculated Unique Customers: {unique_customers_calc:,}")

    # 6. KPI Validation: Return on Investment (ROI)
    # Match this against your Power BI Card visual for ROI
    total_cost_calc = df[COST_COLUMN].sum()
    if total_cost_calc > 0:
        total_profit = total_revenue_calc - total_cost_calc
        roi_calc = (total_profit / total_cost_calc) * 100
        print(f"  - Calculated Total Cost: ₹{total_cost_calc:,.2f}")
        print(f"  - Calculated ROI (Must Match Power BI): {roi_calc:,.2f}%")
    else:
        print("⚠️ ROI Calculation Skipped: Total Cost is zero or negative.")

    # 7. Data Model Check: Date Range
    # Confirm the date range is what you expect for your Date Table creation
    df[MONTH_COLUMN] = pd.to_datetime(df[MONTH_COLUMN])
    min_date = df[MONTH_COLUMN].min().strftime('%Y-%m-%d')
    max_date = df[MONTH_COLUMN].max().strftime('%Y-%m-%d')
    print(f"  - Data Date Range: {min_date} to {max_date}")

except FileNotFoundError:
    print(f"CRITICAL ERROR: File not found at {FILE_PATH}. Update the FILE_PATH variable.")
except KeyError as e:
    print(f"CRITICAL ERROR: Column {e} not found. Check your column names (TOTAL_REVENUE_COLUMN, COST_COLUMN, etc.).")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print("\n--- Testing Complete ---")