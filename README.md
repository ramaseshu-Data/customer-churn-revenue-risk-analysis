# 🚀 Customer Churn & Revenue Risk Analysis (Telecom)

## 📊 Business Problem

Customer churn directly impacts revenue, profitability, and customer lifetime value in telecom businesses.

This project goes beyond basic churn prediction and focuses on:

- Identifying high-risk customer segments
- Quantifying revenue loss due to churn
- Delivering actionable, data-driven business recommendations

---

## 🎯 Key Outcomes

- Built a churn prediction model with ~73% accuracy
- Identified **month-to-month customers as highest churn risk (~43%)**
- Discovered **fiber optic users contribute heavily to churn**
- Estimated **~26% overall churn rate**
- Quantified **revenue at risk (~139K+)**
- Highlighted segments contributing to ~85% of revenue loss

---

## 📁 Dataset

- Source: Telco Customer Churn Dataset (~7000 records)
- Features:
  - Demographics (Gender, Senior Citizen, Dependents)
  - Account Info (Tenure, Contract Type)
  - Services (Internet, Streaming, Tech Support)
  - Billing (Monthly & Total Charges)
- Target Variable: `Churn`

---

## ⚙️ Approach

### 1. Data Preparation
- Removed irrelevant column (`customerID`)
- Converted categorical variables using one-hot encoding
- Validated data quality and handled inconsistencies

### 2. Feature Engineering
- Created binary churn indicator (`Churn_Yes`)
- Structured dataset for machine learning

### 3. Model Development
- Model: Logistic Regression
- Train/Test Split: 80/20
- Handled class imbalance using:
  ```python
  class_weight = 'balanced'4. Model Evaluation
Accuracy: ~73%
Evaluated using:
Confusion Matrix
Precision, Recall, F1-score
Improved recall for churn detection (business-critical)
📈 Key Insights
Month-to-month contracts show highest churn rates
Fiber optic customers churn significantly more than DSL/No-service users
Electronic check users have higher churn probability
Low-tenure customers are at highest risk
💰 Revenue Impact Analysis
Overall churn rate: ~26%
High-risk segments contribute disproportionately to revenue loss
Majority of revenue risk driven by:
Month-to-month contracts
Fiber optic customers

👉 This shifts the project from prediction → business decision-making

📊 Power BI Dashboard

An interactive dashboard was built to translate analysis into business insights:

Key Features:
Total Customers KPI
Churn Customers KPI
Churn Rate KPI
Revenue at Risk KPI
Churn Rate by Contract Type
Churn Rate by Internet Service
Revenue at Risk by Segment
Key Insight:

Month-to-month contracts and fiber optic users contribute to ~85% of revenue at risk.

🧠 Key Drivers of Churn
Contract type
Internet service (Fiber optic)
Payment method
Monthly charges
Customer tenure
📊 Business Recommendations
Promote long-term contracts (1–2 years)
Target retention strategies for fiber optic users
Improve experience for electronic payment customers
Focus retention on low-tenure customers
Introduce loyalty incentives for high-value segments
🛠️ Tech Stack
Python (Pandas, NumPy)
Scikit-learn (Machine Learning)
Power BI (Dashboard & Visualization)
📌 Business Impact

This project demonstrates how analytics can:

Reduce churn risk
Improve retention strategies
Protect revenue

👉 Even a small reduction in churn can significantly increase profitability.

🚀 Future Improvements
Apply advanced ML models (Random Forest, XGBoost)
Deploy model using Streamlit
Automate real-time churn prediction pipeline
👤 Author

Ramashehu
Data Analyst | Business Intelligence | Machine Learning
