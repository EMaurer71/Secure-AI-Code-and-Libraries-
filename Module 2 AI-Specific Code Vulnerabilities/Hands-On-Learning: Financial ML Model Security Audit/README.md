# Final Project — CryptoTrade Pro Security Audit

This folder contains the full CryptoTrade Pro security audit and remediation project.  
This is the final graded lab for the course.
The src folder contains Ai recreted files that should complete the lab as the originals are nto avialble for download.
If that is what you need, feel free to copy those files.

## Purpose
Perform a complete AI/ML security audit of a breached trading platform, including:

- Identifying ML-specific vulnerabilities
- Detecting unsafe deserialization (pickle, joblib)
- Detecting insecure TensorFlow model loading
- Detecting hardcoded secrets
- Detecting OS command injection
- Scanning notebooks for insecure patterns
- Writing custom Semgrep rules
- Implementing secure remediations
- Verifying fixes with Bandit and Semgrep

## Folder Structure

module2_cryptotrade_pro/
│
├── crypto_audit.ipynb        # Main audit notebook (findings)
├── remediation.ipynb         # Remediation notebook (fixes)
│
├── notebooks/
│   └── data_pipeline.ipynb   # Vulnerable notebook
│
├── src/
│   ├── model_management.py           # Vulnerable model loader
│   ├── model_management_fixed.py     # Secure version
│   ├── data_pipeline_fixed.py        # Secure pipeline
│   ├── trading_pipeline.py
│   └── model_loader.py
│
├── rules/
│   ├── pickle-vuln.yaml
│   ├── hardcoded-secrets.yaml
│   └── command-injection.yaml
│
└── trades/
└── data.csv

Code

## How to Run the Audit

Activate your venv, then:

cd module2_cryptotrade_pro
jupyter notebook crypto_audit.ipynb

Code

This notebook will:
- Run Bandit
- Run Semgrep
- Load JSON results
- Generate severity/CWE/file breakdowns
- Auto-number findings (F-01 → F-XX)
- Export a Markdown report

## How to Run the Remediation

jupyter notebook remediation.ipynb

Code

This notebook will:
- Load fixed code
- Run Bandit + Semgrep again
- Compare before vs after
- Produce a remediation summary

## Deliverables
- Audit notebook (`crypto_audit.ipynb`)
- Remediation notebook (`remediation.ipynb`)
- Semgrep rules (`rules/*.yaml`)
- Fixed code (`src/*_fixed.py`)
