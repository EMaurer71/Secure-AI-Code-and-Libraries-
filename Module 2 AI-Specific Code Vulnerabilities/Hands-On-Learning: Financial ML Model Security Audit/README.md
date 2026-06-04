README #2 — Lab: Financial ML Model Security Audit
Location:
Hands-On-Learning: Financial ML Model Security Audit/README.md

Financial ML Model Security Audit — Hands‑On Lab
This folder contains the fully reconstructed and enhanced hands‑on lab for Module 2 of the Coursera course “Secure AI Code & Libraries with Static Analysis.”

In this scenario, you perform a security audit of a financial machine learning pipeline, using static analysis tools, custom Semgrep rules, and CI automation.

The original lab shipped with incomplete instructions and missing files.
I rebuilt the entire environment, added missing components, and created a full GitHub Actions demonstration.

📘 Included Notebooks
1. crypto_audit.ipynb
A full walkthrough of:

Running Bandit, Semgrep, PyLint, and Safety

Identifying ML‑specific vulnerabilities

Reviewing model management and trading pipelines

Documenting findings and severity

2. remediation.ipynb
Maps each vulnerability to:

Severity

Impact

CWE category

Recommended fix

3. deliverables.ipynb
Generates the final:

Security report

Remediation matrix

Supporting evidence

4. GitHub Actions Security Demo
Shows how the CI pipeline runs:

Bandit

Semgrep (custom rules)

PyLint

Safety

Artifact uploads

📁 Custom Semgrep Rules
Folder: rules/

command-injection.yaml

hardcoded-secrets.yaml

pickle-vuln.yaml

These rules detect AI‑specific vulnerabilities not covered by default Semgrep packs.

📁 Source Code
Folder: src/

Includes the intentionally vulnerable ML pipeline:

data_pipeline.ipynb

data_pipeline_fixed.py

model_loader.py

model_management.py

model_management_fixed.py

trading_pipeline.py

And sample trading data:

trades/data.csv

📁 GitHub Actions Workflow
Folder: .github/workflows/

security_scan.yaml  
Runs all static analysis tools and uploads reports.

📁 Security Reports
Folder: security-reports/

Contains raw outputs from:

Bandit

Semgrep

PyLint

Safety

These feed into the final deliverables.

📁 Shell Scripts
Folder: shell_scripts/

run_all_scans.sh

export_reports.sh

These automate local scanning and report generation.

🧠 Why This Lab Matters
This is the most advanced lab in Module 2.
It teaches you how to:

Audit ML pipelines

Detect AI‑specific vulnerabilities

Build custom static analysis rules

Automate security scanning in CI

Produce professional security reports

This lab mirrors real‑world AI security engineering workflows.
