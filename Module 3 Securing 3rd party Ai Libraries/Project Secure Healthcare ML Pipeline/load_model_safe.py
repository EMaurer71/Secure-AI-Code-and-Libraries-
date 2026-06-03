import hashlib
from pathlib import Path
from typing import Any

import joblib

SIG_SUFFIX = ".sig"

def compute_file_hash(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def write_signature(model_path: Path) -> None:
    sig_path = model_path.with_suffix(model_path.suffix + SIG_SUFFIX)
    sig = compute_file_hash(model_path)
    sig_path.write_text(sig)

def verify_signature(model_path: Path) -> None:
    sig_path = model_path.with_suffix(model_path.suffix + SIG_SUFFIX)
    if not sig_path.exists():
        raise ValueError("Missing model signature file")
    expected = sig_path.read_text().strip()
    actual = compute_file_hash(model_path)
    if expected != actual:
        raise ValueError("Model signature mismatch; file may be tampered")

def load_model_safe(path: str = "risk_model.joblib") -> Any:
    model_path = Path(path)
    verify_signature(model_path)
    return joblib.load(model_path)
