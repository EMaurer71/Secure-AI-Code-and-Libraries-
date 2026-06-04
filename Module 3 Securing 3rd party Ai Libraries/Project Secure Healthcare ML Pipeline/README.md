README #4 — Project Secure Healthcare ML Pipeline
Location:
Project Secure Healthcare ML Pipeline/README.md

Project Secure Healthcare ML Pipeline
This folder contains the capstone lab for Module 3 of the Coursera course Secure AI Code & Libraries with Static Analysis.
The original lab shipped with incomplete instructions and missing artifacts.
I rebuilt the entire project, added missing notebooks, and created a complete GitHub Actions workflow.

This project simulates a real‑world healthcare ML pipeline and teaches you how to secure:

Dependencies

Model loaders

Data pipelines

Supply‑chain components

CI/CD workflows

📘 Included Notebooks
1. Module 3 Secure AI Pipeline
Module_3_Secure_AI_Pipeline.ipynb  
A full walkthrough of dependency scanning, SBOM generation, and policy enforcement.

2. GitHub Actions Security Demo
github_actions_healthcare_security_demo.ipynb  
Shows how the CI pipeline runs:

Bandit

Semgrep

PyLint

pip‑audit

Safety

pip‑licenses

CycloneDX

3. Reconstructed Pipeline Notebooks
secure_healthcare_ML_Pipeline.ipynb

secure_healthcare_ml_pipeline.ipynb

secure_healthcare_ml_pipeline_2.ipynb

These were rebuilt from partial course materials.

📁 GitHub Actions Workflow
.github/workflows/security.yml

Runs all dependency and static analysis tools and uploads artifacts.

📁 Reports
Before/after scan results for:

Bandit

Semgrep

PyLint

pip‑audit

Safety

pip‑licenses

SBOM

📁 Source Files
risk_model.py

risk_model_vuln.py

load_model_safe.py

requirements.txt

requirements_vuln.txt

Dataset files

📁 Deliverables
SECURITY_REPORT.md

REFLECTION.txt

🧠 Why This Lab Matters
This project simulates a real‑world healthcare ML pipeline and teaches you how to:

Detect vulnerable dependencies

Enforce security policies

Build CI/CD security gates

Respond to supply‑chain risks

It is the most advanced lab in Module 3.
