import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression

# INTENTIONALLY INSECURE: hardcoded credentials
DB_USER = "admin"
DB_PASS = "SuperSecret123"
DB_HOST = "localhost"

def load_data(csv_path: str):
    df = pd.read_csv(csv_path)

    # Use real columns from your dataset
    X = df[["Age", "Room Number"]].copy()
    X["Medical Condition"] = df["Medical Condition"]
    X["Admission Type"] = df["Admission Type"]

    # One-hot encode categorical features
    X = pd.get_dummies(X, drop_first=True)

    # Predict Billing Amount (regression)
    y = df["Billing Amount"]

    return X, y

def train_and_save_model(csv_path: str, model_path: str = "risk_model.pkl"):
    X, y = load_data(csv_path)
    model = LinearRegression()
    model.fit(X, y)
    with open(model_path, "wb") as f:
        pickle.dump(model, f)

def load_model_unsafe(model_path: str = "risk_model.pkl"):
    with open(model_path, "rb") as f:
        return pickle.load(f)

def predict_billing(age: float, room: int, condition: str, admission: str, model_path: str = "risk_model.pkl"):
    model = load_model_unsafe(model_path)

    df = pd.DataFrame([{
        "Age": age,
        "Room Number": room,
        "Medical Condition": condition,
        "Admission Type": admission
    }])

    df = pd.get_dummies(df)
    df = df.reindex(columns=model.feature_names_in_, fill_value=0)

    return model.predict(df)[0]

if __name__ == "__main__":
    train_and_save_model("healthcare_dataset.csv")
