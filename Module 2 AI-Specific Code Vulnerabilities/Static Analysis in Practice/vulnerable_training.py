
"""
ML Training Pipeline - VULNERABLE VERSION
This script contains multiple security vulnerabilities
"""

import pickle
import pandas as pd
import numpy as np
import boto3
from sklearn.ensemble import RandomForestClassifier
import logging

# VULNERABILITY 1: Hardcoded AWS credentials
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

logging.basicConfig(level=logging.INFO)

def download_training_data(bucket, key):
    """Download training data from S3"""
    # VULNERABILITY 1: Using hardcoded credentials
    s3 = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY
    )

    local_file = 'training_data.csv'
    s3.download_file(bucket, key, local_file)
    return local_file

def load_pretrained_model(model_path):
    """Load pre-trained model"""
    # VULNERABILITY 2: Unsafe pickle deserialization
    # VULNERABILITY 3: Path traversal (model_path from user input)
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    return model

def load_training_data(file_path):
    """Load and prepare training data"""
    # VULNERABILITY 4: No validation on data source
    # VULNERABILITY 4: No file size limits
    # VULNERABILITY 4: No schema validation
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:  # VULNERABILITY 5: Broad exception handling
        logging.error(f"Error loading data: {e}")
        return None

def train_model(model, X, y):
    """Fine-tune the model"""
    # VULNERABILITY 6: No monitoring of training metrics
    model.fit(X, y)

    # VULNERABILITY 7: Logging sensitive information
    logging.info(f"Model trained with {len(X)} samples")
    logging.info(f"AWS Key: {AWS_ACCESS_KEY}")  # CRITICAL: Logging credentials!

    return model

def save_model(model, output_path):
    """Save trained model"""
    # VULNERABILITY 2: Unsafe pickle serialization
    with open(output_path, 'wb') as f:
        pickle.dump(model, f)
    logging.info(f"Model saved to {output_path}")

def main(model_path, data_bucket, data_key, output_path):
    """Main training pipeline"""
    # Download data
    data_file = download_training_data(data_bucket, data_key)

    # Load data
    data = load_training_data(data_file)
    if data is None:
        return

    # Prepare features
    X = data.drop('target', axis=1)
    y = data['target']

    # Load pretrained model
    model = load_pretrained_model(model_path)

    # Train
    trained_model = train_model(model, X, y)

    # Save
    save_model(trained_model, output_path)

    print("Training complete!")

if __name__ == "__main__":
    import sys
    # VULNERABILITY 3: Command line args used without validation
    model_path = sys.argv[1] if len(sys.argv) > 1 else "model.pkl"
    main(model_path, "my-bucket", "data.csv", "output_model.pkl")
