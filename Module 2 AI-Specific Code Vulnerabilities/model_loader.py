# src/model_loader.py

import tensorflow as tf
import pickle

def load_tf_model(path):
    """
    VULNERABLE:
    - tf.keras.models.load_model() with no integrity checks
    """
    return tf.keras.models.load_model(path)

def load_pickle_model(path):
    """
    VULNERABLE:
    - generic pickle.load() wrapper
    """
    with open(path, "rb") as f:
        return pickle.load(f)

