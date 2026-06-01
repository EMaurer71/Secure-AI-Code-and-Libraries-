import pickle
import joblib
import tensorflow as tf
import requests
import os

# F-07, F-08, F-09 – hardcoded secrets
DB_PASSWORD = "SuperSecret99"
DB_USER = "admin"
BINANCE_API_KEY = "vmPUZE6mv9SD5VNHk4HlbGhAKLFmtOtaGO5jXmM87C1"
BINANCE_SECRET = "NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65y2H"
COINBASE_API_TOKEN = "Bearer prod_abc123_secret_token_here"
AWS_ACCESS_KEY_ID = "AKIAI44QH8DHBEXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

MODELS_DIR = "/app/models"


def load_model_direct(model_path: str):
    """
    F-01 – Direct pickle.load()
    """
    with open(model_path, "rb") as f:
        model = pickle.load(f)  # UNSAFE
    return model


def load_model_from_user_input(user_provided_path: str):
    """
    F-02 – User-controlled path + pickle.load()
    """
    model_dir = "/app/models/"
    full_path = model_dir + user_provided_path  # no sanitization
    with open(full_path, "rb") as f:
        model = pickle.load(f)  # CRITICAL
    return model


def load_model_from_api(url: str):
    """
    F-03 – pickle.loads() on network data
    """
    resp = requests.get(url)
    data = resp.content
    model = pickle.loads(data)  # CRITICAL
    return model


def load_model_with_false_safety(path: str):
    """
    F-04 – pickle.load() in try/except (false safety)
    """
    try:
        with open(path, "rb") as f:
            model = pickle.load(f)  # still unsafe
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None


def load_tf_model(path: str):
    """
    F-05 – Unsafe tf.keras.models.load_model()
    """
    model = tf.keras.models.load_model(path)  # no integrity check
    return model


def load_joblib_model(path: str):
    """
    F-06 – Unsafe joblib.load() (no hash check)
    """
    model = joblib.load(path)  # uses pickle internally
    return model

