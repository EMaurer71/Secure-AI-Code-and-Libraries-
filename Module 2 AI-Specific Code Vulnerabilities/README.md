Module 2 — AI‑Specific Code Vulnerabilities
This module contains my reconstructed and expanded work for Module 2 of the Coursera course “Secure AI Code & Libraries with Static Analysis.”  
The goal of this module is to understand and detect AI‑specific coding vulnerabilities that traditional software security tools often miss.

The module is divided into two major parts:

Classroom Walkthrough — Common AI Code Vulnerabilities

Static Analysis in Practice — ML Pipeline Vulnerability Hunt

Both sections were enhanced to include missing logic, clearer examples, and runnable code.

📘 Part 1 — Classroom Walkthrough: Common AI Code Vulnerabilities
Folder:
Common AI Code Vulnerabilities/

This section contains five demonstration notebooks, each focused on a specific AI/ML security weakness:

1. Insecure Pickle Deserialization
01_insecure_pickle_deserialization.ipynb  
Shows how unsafe model loading can lead to arbitrary code execution.

2. Hardcoded Credentials
02_hardcoded_credentials.ipynb  
Demonstrates credential leakage in ML pipelines and training scripts.

3. Path Traversal in Model Loading
03_path_traversal_model_loading.ipynb  
Explains how user‑controlled paths can compromise model integrity.

4. Unsafe Data Pipelines
04_unsafe_data_pipeline.ipynb  
Shows how unvalidated data flows can lead to poisoning or corruption.

5. Dependency Confusion
05_dependency_confusion.ipynb  
Demonstrates how ML environments are vulnerable to malicious package injection.

These notebooks were reconstructed to be fully runnable and include additional examples not present in the original course.

📙 Part 2 — Static Analysis in Practice
Folder:
Static Analysis in Practice/

This section applies static analysis tools to real ML codebases.

1. ML Pipeline Vulnerability Hunt
01_ml_pipeline_vulnerability_hunt.ipynb  
A guided walkthrough of identifying vulnerabilities in ML training and inference code.

2. Custom Semgrep Rules
02_custom_semgrep_rules.ipynb  
Demonstrates how to write Semgrep rules for AI‑specific issues using:
ml-security-rules.yml

3. Notebook Scanning with Semgrep
03_notebook_scanning_with_semgrep.ipynb  
Shows how to scan .ipynb files for insecure patterns.

Supporting Code
secure_training.py

vulnerable_training.py

These scripts provide the codebase used for static analysis.

📘 Hands‑On Lab — Financial ML Model Security Audit
Folder:
Hands-On-Learning: Financial ML Model Security Audit/

This lab required full reconstruction due to missing instructions and incomplete artifacts.
It now includes:

A complete ML security audit

Custom Semgrep rules

GitHub Actions CI pipeline

Security reports

Remediation matrix

Rebuilt notebooks and scripts

See the dedicated README below.

🧠 Why This Module Matters
This module teaches you how to identify and remediate vulnerabilities unique to AI/ML systems, including:

Unsafe model loading

Data pipeline risks

Dependency and supply‑chain attacks

Notebook‑specific vulnerabilities

ML‑specific static analysis rules

These skills prepare you for the full security audit in the hands‑on lab.
