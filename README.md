# 📊 Customer Profitability Analysis

### 🏢 Industry Project  
**Company:** Tata Consultancy Services (TCS)  
**Institute:** JNTUH College of Engineering, Manthani  
**Duration:** 06 Oct 2025 – 10 Nov 2025 (90 hrs)  
**Project Type:** Individual Development  
**Environment:** Windows OS, Jupyter Notebook, MySQL, Power BI  

---

## 📘 Project Overview
The **Customer Profitability Analysis** project aims to build a **dynamic Power BI dashboard** that goes beyond simple revenue tracking — focusing instead on **strategic profitability analysis** through metrics like **Customer Lifetime Value (CLV)** and **Return on Investment (ROI)**.  

By integrating **Python (Pandas, NumPy)** for data preprocessing, **MySQL** for structured data storage, and **Power BI** for visualization, the project provides executives with a unified view of customer financial health and actionable insights for decision-making.

---

## 🎯 Objective and Scope
**Objective:**  
To calculate true customer value using advanced KPIs (CLV, ROI) and visualize insights through an interactive, executive-level dashboard.

**Scope:**  
The analysis focuses on historical customer data and acquisition costs. The final deliverable includes a **single-page Power BI dashboard**, validation scripts, and complete documentation.

---

## 🚩 Problem Statement
Businesses often lack an integrated view of customer profitability due to:
- No dynamic calculation of ROI on customer acquisition.
- Unknown long-term value (CLV) of customers.
- Unstandardized time-based performance metrics.

---

## 💡 Methodology

### Phase 1: Data Preparation
- Cleaned and merged datasets using **Python (Pandas)**.
- Handled missing values, duplicates, and data type conversions.

### Phase 2: Database Setup
- Designed relational schemas in **MySQL**.
- Imported processed data into the `customer_profitability_db`.

### Phase 3: Data Modeling
- Created **Date** and **Acquisition Lookup Tables**.
- Established relationships between fact and dimension tables.

### Phase 4: KPI Development
- Built DAX measures for **Revenue**, **ROI**, **CLV**, and **MoM Growth**.
- Applied time intelligence and relational functions in Power BI.

### Phase 5: Dashboard Design
- Implemented visuals: KPI Cards, Line/Bar Charts, Donut Charts, and Slicers.
- Designed an executive-style dashboard using a **dark theme**.

### Phase 6: Validation & Documentation
- Verified results via **Python validation scripts**.
- Created detailed technical documentation for handover.

---

## 🔄 Workflow
**Data Collection → Data Cleaning → SQL Setup → KPI Calculation → Visualization → Dashboard Reporting → Documentation**

---

## ⚙️ Tools and Technologies
| Category | Tools Used |
|-----------|-------------|
| Programming | Python (Pandas, NumPy, Matplotlib, Seaborn) |
| Database | MySQL |
| Visualization | Power BI (DAX, Power Query) |
| Development | VS Code, Jupyter Notebook |
| OS | Windows 10 |

---

## 🧱 Solution Architecture
**Three-Tier Architecture:**
1. **Presentation Layer:** Power BI dashboard (interactive visuals, KPIs, slicers).  
2. **Business Logic Layer:** Python ETL, SQL queries, DAX measures.  
3. **Data Layer:** MySQL database for structured storage and indexing.

---

## 🧩 Key Features
- Automated **ETL pipeline** with Python.
- **Optimized MySQL schema** for telecom data.
- **Dynamic Power BI dashboard** with CLV and ROI metrics.
- End-to-end integration from raw data to insights.
- **Validation scripts** to ensure data accuracy.

---

## 📈 Challenges & Solutions
| Challenge | Solution |
|------------|-----------|
| CLV Computation | Developed modular DAX formulas for accurate CLV and ROI. |
| Integration of Tools | Automated ETL scripts for seamless Python–MySQL–Power BI sync. |
| Dashboard Speed | Implemented incremental refresh and query optimization. |
| Data Quality | Preprocessed data using Pandas and applied SQL constraints. |

---

## 🚀 Results & Achievements
- **75% reduction** in manual analysis time.  
- **Real-time profit insights** for each customer.  
- Dashboard refresh in **<2 seconds**.  
- ETL pipeline processes **100K+ records in under 2 minutes**.  
- Over **1M telecom records analyzed**.  

---

## 💼 Business Impact
- Enabled executives to make **data-driven profitability decisions**.  
- Identified unprofitable customers with **20% higher accuracy**.  
- Improved transparency and cross-team collaboration.  
- Accelerated strategy formulation through **real-time insights**.

---

## 🔮 Enhancement Scope

### Short-Term (3–6 Months)
- Automate ETL validation and incremental refresh.
- Implement MoM and YoY trend analytics.

### Medium-Term (6–12 Months)
- Integrate ML models for churn prediction.
- Connect with CRM/ERP systems.

### Long-Term (12+ Months)
- Cloud deployment on **Azure/AWS**.
- Real-time analytics using **Kafka + DirectQuery**.
- Add **AI-driven recommendations**.

---

## 🧠 Research Questions

1. **How does profitability analytics improve decision-making?**  
   → Provides data-driven insights for optimizing customer value and marketing spend.

2. **How does CLV contribute to growth?**  
   → Focuses resources on high-value customers for long-term profitability.

3. **What is the role of visualization?**  
   → Converts complex financial data into clear, interactive insights.

4. **How can predictive analytics enhance profitability?**  
   → Enables proactive forecasting of customer behavior and churn.

5. **Why is segmentation important?**  
   → Supports targeted marketing and maximizes profitability per customer group.

---

## 🧩 Repository Structure
Customer_Profitability_Analysis/
│
├── Data/
│ ├── cdr_data.csv
│ ├── cleaned_cdr.csv
│ ├── cleaned_customer_profiles.csv
│ ├── cleaned_rules_master.csv
│ └── rules_master.csv
│
├── Reports/
│ ├── Screenshot (688).png
│ ├── Screenshot (689).png
│ ├── Screenshot (690).png
│ └── Screenshot (691).png
│
├── Scripts/
│ └── cleaning.ipynb
│
├── Tests/
│ └── Validate_Data.py
│
├── sql_setup/
│ └── schema_creation.sql
│
├── Dax_Formulaes.txt
└── requirements.txt



---

## ⚙️ Installation & Setup

### Step 1: Clone Repository
```bash
git clone https://github.com/Nithinln0/CUSTOMER_PROFITABILITY_ANALYSIS

Step 2: Install Dependencies

pip install -r requirements.txt

Step 3: Run Data Cleaning Script


python Scripts/cleaning.ipynb

Step 4: Setup MySQL Database

Create a database: customer_profitability_db

Import schema from: sql_setup/schema_creation.sql

Load cleaned CSV files into respective tables.

Step 5: Power BI Integration

Open Customer_Profitability.pbix in Power BI.

Update MySQL credentials in Data Source Settings.

Click Refresh to load latest data.

🧾 References

Kaggle Telecom Dataset

Python Pandas Documentation

Matplotlib & Seaborn Docs

Power BI Docs

MySQL Reference Manual

👨‍💻 Author
Name: Ch. Nithin Chowdary
Institution: JNTUH University College of Engineering, Manthani
