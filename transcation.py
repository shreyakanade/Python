import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Load data
data = pd.read_csv('payment_data.csv')

# Preprocessing
# (Include data cleaning, feature engineering, encoding categorical variables, etc.)

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(data.drop('is_fraud', axis=1), data['is_fraud'], test_size=0.2, random_state=42)

# Train logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
print(classification_report(y_test, y_pred))
