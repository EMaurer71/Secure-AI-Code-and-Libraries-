README #3 — Tools for Dependency & License Analysis
Location:
Tools for Dependency & License Analysis/README.md

Tools for Dependency & License Analysis
This folder contains the second classroom demonstration for Module 3 — Securing 3rd‑Party AI Libraries.
It introduces the tools used to detect vulnerabilities, license issues, and supply‑chain risks in AI/ML environments.

📘 Notebook Included
Tools for Dependency & License Analysis
File: module_3_tools_dependency_license_analysis.ipynb

This notebook demonstrates:

🔍 1. Static Analysis Tools
Bandit

Semgrep

PyLint

📦 2. Dependency Scanning
pip‑audit

Safety

📜 3. License Compliance
pip‑licenses

📄 4. SBOM Generation
CycloneDX

JSON and CSV formats

🧪 5. Before/After Comparison
The notebook includes:

Vulnerable requirements

Secure requirements

Before/after scan reports

📁 Supporting Files
requirements_vulnerable.txt

security_gate_config.json

sbom.json

load_model_safe.py

Before‑scan reports in reports/

🧠 Why This Demo Matters
Dependency and license analysis is essential for:

Preventing supply‑chain attacks

Ensuring compliance

Maintaining secure ML environments

Building CI/CD security gates

This demo prepares you for the Module 3 labs.
