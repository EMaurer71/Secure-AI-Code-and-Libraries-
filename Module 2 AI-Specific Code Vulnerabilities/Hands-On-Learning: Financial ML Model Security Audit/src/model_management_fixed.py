# cryptotrade_pro/src/model_management_fixed.py

import hashlib
import os
import joblib
import onnxruntime as ort

ALLOWED_MODELS = {"baseline_model.onnx", "prod_model.onnx"}
MODELS_DIR = "/app/models"
HASH_MANIFEST = {
    # filename: sha256
    "baseline_model.onnx": "REPLACE_WITH_REAL_HASH",
    "prod_model.onnx": "REPLACE_WITH_REAL_HASH",
}


def _verify_hash(path: str, expected_hash: str) -> bool:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest() == expected_hash


def load_onnx_model(name: str):
    """
    Secure replacement for pickle/tf/joblib loading.
    """
    if name not in ALLOWED_MODELS:
        raise ValueError("Model not allowed")

    full_path = os.path.join(MODELS_DIR, name)
    expected = HASH_MANIFEST.get(name)
    if not expected or not _verify_hash(full_path, expected):
        raise ValueError("Model integrity check failed")

    return ort.InferenceSession(full_path)


def load_joblib_model_verified(path: str, expected_hash: str):
    """
    Residual risk: joblib.load() with pre-load hash verification.
    """
    if not _verify_hash(path, expected_hash):
        raise ValueError("Hash mismatch")
    return joblib.load(path)

