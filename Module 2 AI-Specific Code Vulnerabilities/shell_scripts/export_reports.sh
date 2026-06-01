#!/bin/bash

echo "=== Packaging CryptoTrade Pro Deliverables ==="

mkdir -p deliverables
mkdir -p deliverables/security-reports
mkdir -p deliverables/rules
mkdir -p deliverables/fixed_code

echo "[1/6] Copying security reports"
cp security-reports/*.json deliverables/security-reports/

echo "[2/6] Copying notebooks (raw .ipynb files)"
cp crypto_audit.ipynb deliverables/
cp remediation.ipynb deliverables/

echo "[3/6] Copying Semgrep rules"
cp rules/*.yaml deliverables/rules/

echo "[4/6] Copying fixed code"
cp src/*_fixed.py deliverables/fixed_code/

echo "[5/6] Checking for remediation report"
if [ -f deliverables/Remediation_Report.md ]; then
    echo "Found remediation report."
else
    echo "No remediation report found — skipping."
fi

echo "[6/6] Creating ZIP file"
cd deliverables
zip -r CryptoTradePro_Submission.zip ./*
cd ..

echo "=== Deliverables packaged successfully ==="
echo "File created: deliverables/CryptoTradePro_Submission.zip"

