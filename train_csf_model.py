import pandas as pd
from catboost import CatBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import numpy as np

np.random.seed(42)
data_size = 500

data = pd.DataFrame({
    "production_time": np.random.randint(10, 50, data_size),
    "downtime_percent": np.random.randint(1, 20, data_size),
    "delivery_rate": np.random.randint(70, 100, data_size),

    "supplier_score": np.random.randint(50, 100, data_size),
    "inventory_days": np.random.randint(5, 30, data_size),
    "price_volatility": np.random.randint(1, 15, data_size),

    "complaint_count": np.random.randint(0, 10, data_size),
    "response_time": np.random.randint(1, 24, data_size),
    "nps_score": np.random.randint(0, 10, data_size),

    "carbon_emission": np.random.randint(1, 20, data_size),
    "energy_efficiency": np.random.randint(50, 100, data_size),
    "recycling_rate": np.random.randint(40, 100, data_size),
})

data["customer_satisfaction"] = (
    (data["delivery_rate"] > 85) &
    (data["supplier_score"] > 70) &
    (data["complaint_count"] < 5) &
    (data["energy_efficiency"] > 70)
).astype(int)

X = data.drop("customer_satisfaction", axis=1)
y = data["customer_satisfaction"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = CatBoostClassifier(verbose=0)
model.fit(X_train, y_train)

print("Accuracy:", accuracy_score(y_test, model.predict(X_test)))

joblib.dump(model, "csf_catboost_model.pkl")
print("Model saved!")
