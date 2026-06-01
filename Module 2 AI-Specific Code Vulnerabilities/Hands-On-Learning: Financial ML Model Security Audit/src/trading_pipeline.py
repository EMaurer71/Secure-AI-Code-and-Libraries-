# src/trading_pipeline.py

from model_management import load_model
import pandas as pd

def run_trading_session(model_name, trades_csv="data/trades.csv"):
    """
    VULNERABLE:
    - model_name may come from user input / config
    - loads untrusted pickle
    """
    model = load_model(model_name)
    trades = pd.read_csv(trades_csv)
    features = trades[["price", "volume", "volatility"]]
    preds = model.predict(features)
    return preds

if __name__ == "__main__":
    import sys
    model_name = sys.argv[1] if len(sys.argv) > 1 else "prod_model"
    preds = run_trading_session(model_name)
    print("Executed trading session with", len(preds), "predictions.")

