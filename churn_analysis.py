import pandas as pd

df = pd.read_csv("Telco-Customer-Churn.csv")

# Fix TotalCharges (THIS IS THE KEY CHANGE)
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors='coerce')

# Remove null values
df = df.dropna()

# Then drop ID
df = df.drop("customerID", axis=1)

# Then encoding
df = pd.get_dummies(df, drop_first=True)

print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.head())
X = df.drop("Churn_Yes", axis=1)
y = df["Churn_Yes"]
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000, class_weight='balanced')
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(y_pred[:10])
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

print("Accuracy:", accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': model.coef_[0]
})

feature_importance = feature_importance.sort_values(by='Importance', ascending=False)

print(feature_importance.head(10))
churn_rate = df["Churn_Yes"].mean()
print("Churn Rate:", churn_rate)
avg_revenue = df["MonthlyCharges"].mean()
lost_revenue = df[df["Churn_Yes"] == 1]["MonthlyCharges"].sum()
print(df.columns)
print(df.groupby("Contract_One year")["Churn_Yes"].mean())
print(df.groupby("Contract_Two year")["Churn_Yes"].mean())
print(df.groupby("InternetService_Fiber optic")["Churn_Yes"].mean())