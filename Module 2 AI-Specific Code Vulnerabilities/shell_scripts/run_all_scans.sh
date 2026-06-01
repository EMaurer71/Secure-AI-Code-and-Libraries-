#!/bin/bash

echo "=== CryptoTrade Pro: Running Full Security Scan (No Jupyter Required) ==="

# Create output folder
mkdir -p security-reports

echo "[1/7] Running Bandit on src/"
bandit -r src -f json -o security-reports/bandit-src.json

echo "[2/7] Running Semgrep (pickle rule)"
semgrep --config rules/pickle-vuln.yaml src --json --output security-reports/semgrep-pickle.json

echo "[3/7] Running Semgrep (hardcoded secrets)"
semgrep --config rules/hardcoded-secrets.yaml src --json --output security-reports/semgrep-secrets.json

echo "[4/7] Running Semgrep (command injection)"
semgrep --config rules/command-injection.yaml src --json --output security-reports/semgrep-cmd.json

echo "[5/7] Extracting notebook to Python (manual extraction)"
# If Jupyter isn't installed, we manually extract code cells using grep
grep -R \"source\": notebooks/data_pipeline.ipynb \
    | sed 's/.*\"source\": \

\[//; s/\\]

,.*//' \
    | sed 's/\\\\n/\\n/g' \
    | sed 's/\"//g' \
    > security-reports/data_pipeline.py

echo "[6/7] Running Bandit on extracted notebook code"
bandit -r security-reports/data_pipeline.py -f json -o security-reports/bandit-notebook.json

echo "[7/7] Running Semgrep on extracted notebook code"
semgrep --config rules/hardcoded-secrets.yaml security-reports/data_pipeline.py --json --output security-reports/semgrep-notebook.json

echo "=== All scans complete. Reports saved in security-reports/ ==="
ls -l security-reports

