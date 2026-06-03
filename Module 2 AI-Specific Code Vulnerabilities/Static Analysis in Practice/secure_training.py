
"""
ML Training Pipeline - SECURE VERSION
All vulnerabilities have been fixed
"""

import joblib
import pandas as pd
import numpy as np
import boto3
import os
import logging
from pathlib import Path

# FIX 1: Use environment variables / IAM roles for credentials
# Do NOT hardcode AWS keys in source code.

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# FIX 3: Whitelist of allowed models
ALLOWED_MODELS = ['baseline_model', 'pretrained_model', 'production_model']

def download_training_data(bucket, key):
    """Download training data from S3"""
    # FIX 1: Use boto3's credential chain (env vars, IAM roles, etc.)
    s3 = boto3.client('s3')
    local_file = 'training_data.csv'
    try:
        s3.download_file(bucket, key, local_file)
        logging.info("Training data downloaded successfully")
        return local_file
    except Exception as e:
        logging.error("Failed to download training data")
        raise

def load_pretrained_model(model_name):
    """Load pre-trained model with security checks"""
    # FIX 3: Validate model name against whitelist
    if model_name not in ALLOWED_MODELS:
        raise ValueError(f"Invalid model name. Allowed: {ALLOWED_MODELS}")

    model_path = Path('models') / f"{model_name}.joblib"

    # Ensure path stays within models directory
    if not str(model_path.resolve()).startswith(str(Path('models').resolve())):
        raise ValueError("Path traversal attempt detected")

    try:
        model = joblib.load(model_path)
        logging.info(f"Model loaded: {model_name}")
        return model
    except FileNotFoundError:
        logging.error(f"Model file not found: {model_path}")
        raise

def load_training_data(file_path):
    """Load and validate training data"""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Data file not found: {file_path}")

    file_size = os.path.getsize(file_path)
    max_size = 100 * 1024 * 1024  # 100MB
    if file_size > max_size:
        raise ValueError(f"File too large: {file_size} bytes")

    try:
        data = pd.read_csv(file_path)
        required_columns = ['target']
        if not all(col in data.columns for col in required_columns):
            raise ValueError("Missing required columns")

        if data.isnull().sum().sum() > len(data) * 0.5:
            logging.warning("High percentage of missing values detected")

        logging.info(f"Data loaded: {len(data)} rows, {len(data.columns)} columns")
        return data
    except Exception:
        logging.error("Failed to load or validate data")
        raise

def train_model(model, X, y):
    """Fine-tune the model"""
    if len(X) != len(y):
        raise ValueError("Feature and target length mismatch")
    if len(X) < 10:
        raise ValueError("Insufficient training data")

    model.fit(X, y)
    logging.info(f"Model trained successfully with {len(X)} samples")
    logging.info(f"Feature dimensions: {X.shape}")
    return model

def save_model(model, output_path):
    """Save trained model securely"""
    try:
        joblib.dump(model, output_path)
        logging.info(f"Model saved to {output_path}")
    except Exception:
        logging.error("Failed to save model")
        raise

def main(model_name, data_bucket, data_key, output_path):
    """Main training pipeline with error handling"""
    try:
        data_file = download_training_data(data_bucket, data_key)
        data = load_training_data(data_file)
        X = data.drop('target', axis=1)
        y = data['target']
        model = load_pretrained_model(model_name)
        trained_model = train_model(model, X, y)
        save_model(trained_model, output_path)
        print("✅ Training complete!")
    except Exception as e:
        logging.error(f"Training pipeline failed: {type(e).__name__}")
        raise

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python secure_training.py <model_name>")
        print(f"Allowed models: {ALLOWED_MODELS}")
        sys.exit(1)
    model_name = sys.argv[1]
    main(model_name, "my-bucket", "data.csv", "output_model.joblib")
