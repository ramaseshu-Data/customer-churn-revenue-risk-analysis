🚀 Customer Churn & Revenue Risk Analysis (Telecom)
📊 Dashboard Preview

🎯 Business Objective

Customer churn is a major revenue leakage point in telecom.

This project goes beyond prediction and focuses on:

Identifying high-value customers at risk of churn
Quantifying revenue exposure
Recommending targeted retention strategies
💡 Key Business Impact
~26% customers at risk of churn
Estimated ~139K+ revenue exposed to churn
Top 20% high-risk customers contribute to majority of revenue loss
Targeting these customers can significantly reduce revenue leakage

👉 Insight: Not all churn is equal — prioritization is critical

🧠 Analytical Approach
Data Processing
Cleaned and validated dataset (~7000 records)
Applied one-hot encoding
Engineered churn binary variable
Modeling
Logistic Regression with class_weight='balanced'
Train/Test split: 80/20
Evaluation
Accuracy: ~73%
Focus on Recall (churn detection) over accuracy
🔍 Key Drivers of Churn

Top influencing factors:

Contract Type (Month-to-Month)
Tenure (Low tenure = high risk)
Internet Service (Fiber Optic)
Payment Method (Electronic Check)
Monthly Charges

👉 These are actionable business levers

📊 Customer Risk Segmentation

Customers were segmented based on:

Churn probability
Revenue contribution
Segments:
🔴 High Risk + High Value → Immediate retention focus
🟠 High Risk + Low Value → Selective targeting
🟢 Low Risk + High Value → Loyalty programs
⚪ Low Risk + Low Value → Minimal focus

👉 This enables cost-efficient retention strategy

💰 Revenue Impact Simulation

Instead of just measuring churn, we simulate business impact:

If churn reduced by 10% → Significant revenue recovery
Targeting top high-risk segments yields maximum ROI

👉 Focus should be on:

Month-to-month contracts
Fiber optic users
Low tenure high spenders
📊 Power BI Dashboard
Features:
Churn Rate KPI
Revenue at Risk KPI
Segment-wise churn analysis
Contract & service breakdown
Risk-based revenue visualization
Key Insight:

~85% of revenue at risk comes from a small group of high-risk customers

📌 Business Recommendations
Convert month-to-month → long-term contracts
Improve service quality for fiber users
Introduce retention offers for high-value customers
Target low-tenure customers early
Optimize pricing / payment experience
🛠️ Tech Stack
Python (Pandas, NumPy)
Scikit-learn
Power BI
🚀 What Makes This Project Different

Unlike basic churn projects, this analysis:

Connects ML predictions → revenue impact
Prioritizes customers based on business value
Provides actionable retention strategy

👉 Focus is on decision-making, not just prediction

🔮 Future Enhancements
Advanced models (XGBoost, Random Forest)
Real-time churn monitoring pipeline
Deployment using Streamlit


👤 Author

Ramashehu
Data Analyst | SQL | Power BI | Machine Learning
