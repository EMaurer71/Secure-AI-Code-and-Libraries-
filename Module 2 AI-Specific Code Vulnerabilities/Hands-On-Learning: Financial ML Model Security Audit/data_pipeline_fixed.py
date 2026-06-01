# cryptotrade_pro/src/data_pipeline_fixed.py

import pandas as pd
import os
import logging

logging.basicConfig(level=logging.INFO)

# Secrets now from environment
BINANCE_API_KEY = os.environ.get("BINANCE_API_KEY")
BINANCE_SECRET = os.environ.get("BINANCE_SECRET")
COINBASE_API_TOKEN = os.environ.get("COINBASE_API_TOKEN")
aws_key = os.environ.get("AWS_ACCESS_KEY_ID")
DB_CONNECTION = os.environ.get("DB_CONNECTION_STRING")


def preprocess_data(symbol: str):
    """
    Secure: no os.system, just logging.
    """
    if not symbol.isalpha():
        raise ValueError("Invalid symbol")
    logging.info("Fetching data for %s", symbol)


def run_data_export(symbol: str):
    """
    Secure: no shell=True, no f-strings.
    """
    if not symbol.isalpha():
        raise ValueError("Invalid symbol")
    # In a real system, call a safe Python function instead of shelling out.
    logging.info("Exporting data for %s", symbol)


def load_trades():
    path = os.path.join("data", "trades.csv")
    df = pd.read_csv(path)
    if df.shape[0] > 1_000_000:
        raise ValueError("File too large")
    return df

