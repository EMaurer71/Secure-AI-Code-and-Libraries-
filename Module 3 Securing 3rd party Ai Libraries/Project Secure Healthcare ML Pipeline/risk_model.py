import os
from pathlib import Path
from typing import Tuple

import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from dotenv import load_dotenv

from load_model_safe import write_signature, load_model_safe

load_dotenv()

DATA_PATH = Path("healthcare_dataset.csv")

def load_data(path: Path) -> Tuple[pd.DataFrame, pd.Series]:
    df = pd.read_csv(path)

    # Use real columns from your dataset
    X = df[["Age", "Room Number"]].copy()
    X["Medical Condition"] = df["Medical Condition"]
    X["Admission Type"] = df["Admission Type"]

    # One-hot encode categorical features
    X = pd.get_dummies(X, drop_first=True)

    # Predict Billing Amount
    y = df["Billing Amount"]

    return X, y

def train_model(X, y) -> LinearRegression:
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def save_model(model, path: str = "risk_model.joblib"):
    joblib.dump(model, path)
    write_signature(Path(path))

def validate_inputs(age: float, room: int, condition: str, admission: str) -> None:
    if not (0 < age < 120):
        raise ValueError("Age out of range")
    if not (1 <= room <= 999):
        raise ValueError("Room number out of range")
    if not isinstance(condition, str):
        raise ValueError("Invalid medical condition")
    if not isinstance(admission, str):
        raise ValueError("Invalid admission type")

def predict_billing(
    age: float,
    room: int,
    condition: str,
    admission: str,
    model_path: str = "risk_model.joblib",
):
    validate_inputs(age, room, condition, admission)
    model = load_model_safe(model_path)

    df = pd.DataFrame(
        [{
            "Age": age,
            "Room Number": room,
            "Medical Condition": condition,
            "Admission Type": admission,
        }]
    )

    df = pd.get_dummies(df)
    df = df.reindex(columns=model.feature_names_in_, fill_value=0)

    return model.predict(df)[0]

if __name__ == "__main__":
    X, y = load_data(DATA_PATH)
    model = train_model(X, y)
    save_model(model)
