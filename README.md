🚀 Customer Churn & Revenue Risk Analysis (Telecom)


📊 Overview

Customer churn is a critical business problem in the telecom industry, directly impacting revenue, profitability, and customer lifetime value.

In this project, I analyzed telecom customer data to:

Identify high-risk customer segments
Quantify revenue loss due to churn
Deliver actionable business recommendations
🎯 Business Objectives
Predict customer churn using machine learning
Identify key drivers influencing churn
Segment high-risk customers
Estimate revenue loss from churn
Provide data-driven retention strategies
📁 Dataset
Source: Telco Customer Churn Dataset (~7000 records)
Key Features:
Demographics (Gender, Senior Citizen, Dependents)
Account Info (Tenure, Contract Type)
Services (Internet, Streaming, Tech Support)
Billing (Monthly Charges, Total Charges)
Target Variable: Churn
⚙️ Approach
1. Data Preprocessing
Removed irrelevant column (customerID)
Converted categorical variables using one-hot encoding
Validated data quality and missing values
2. Feature Engineering
Created binary churn variable (Churn_Yes)
Prepared dataset for modeling
3. Model Building
Model: Logistic Regression
Train-Test Split: 80/20
Handled class imbalance using:
class_weight = 'balanced'
4. Model Evaluation
Accuracy Score: ~73%
Evaluated using Confusion Matrix and Classification Report
Balanced recall improved for churn prediction
📈 Key Insights
Customers with month-to-month contracts show significantly higher churn (~30%+)
Fiber optic users have higher churn rates compared to other service types
Customers using electronic check payments are more likely to churn
Low-tenure customers are at highest risk
💰 Revenue Impact Analysis
Average churn rate: ~26%
Estimated monthly revenue loss from churn: significant portion of total revenue
High-risk segments contribute disproportionately to revenue loss

👉 This shifts the analysis from prediction → business impact and revenue risk

🧠 Key Drivers of Churn

Top influencing factors identified:

Contract type
Internet service (Fiber optic)
Payment method
Monthly charges
Customer tenure
📊 Business Recommendations
Encourage customers to move to long-term contracts (1–2 years)
Provide targeted retention offers for fiber optic users
Improve experience for electronic payment users
Focus retention strategies on low-tenure customers
Introduce loyalty incentives for high-value customers
📊 Power BI Dashboard (Next Phase)

To enhance business usability, this project can be extended with a dashboard including:

Churn Rate KPI
Revenue Loss KPI
Churn by Contract Type
Churn by Payment Method
Customer Segmentation
🛠️ Tech Stack
Python (Pandas, NumPy)
Scikit-learn
Data Preprocessing & Machine Learning
Power BI (planned for visualization)
📌 Business Impact
Identified high-risk segments driving churn
Quantified churn impact on revenue
Provided actionable retention strategies

👉 Even a 5% reduction in churn can lead to substantial annual revenue savings.

🚀 Future Improvements
Apply advanced models (Random Forest, XGBoost)
Build interactive Power BI dashboard
Deploy model using Streamlit
Automate pipeline for real-time prediction
👤 Author

Ramashehu
Data Analyst | Business Intelligence | Machine Learning
