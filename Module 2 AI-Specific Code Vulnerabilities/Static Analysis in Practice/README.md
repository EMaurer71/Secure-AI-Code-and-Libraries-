README — Static Analysis in Practice
Location:
Module 2 AI-Specific Code Vulnerabilities/Static Analysis in Practice/README.md

Static Analysis in Practice
This folder contains the second half of Module 2 — AI‑Specific Code Vulnerabilities from the Coursera course Secure AI Code & Libraries with Static Analysis.
Here, you apply static analysis tools to real ML codebases and learn how to detect AI‑specific vulnerabilities at scale.

This section bridges the gap between conceptual vulnerabilities and real‑world security engineering.

🎯 Learning Objectives
This section teaches you to:

Apply static analysis tools to ML pipelines

Detect insecure patterns in training and inference code

Write custom Semgrep rules for AI‑specific issues

Scan Jupyter notebooks for vulnerabilities

Interpret findings and map them to remediation steps

Prepare for the full financial ML security audit lab

📘 Included Notebooks
1. ML Pipeline Vulnerability Hunt
File: 01_ml_pipeline_vulnerability_hunt.ipynb  
A guided walkthrough of identifying vulnerabilities in:

Model training scripts

Data ingestion pipelines

Model management logic

Inference code

You analyze both secure and intentionally vulnerable versions of the pipeline.

2. Custom Semgrep Rules
File: 02_custom_semgrep_rules.ipynb  
Demonstrates how to write Semgrep rules for AI‑specific issues using:

ml-security-rules.yml

secure_training.py

vulnerable_training.py

You learn how to detect:

Unsafe model loading

Hardcoded secrets

Dangerous file operations

Insecure data flows

3. Notebook Scanning with Semgrep
File: 03_notebook_scanning_with_semgrep.ipynb  
Shows how to scan .ipynb files for:

Insecure code cells

Hidden secrets

Unsafe imports

Dangerous execution patterns

This is critical because many ML teams rely heavily on notebooks.

📁 Supporting Files
ml-security-rules.yml
A custom Semgrep rule pack for AI‑specific vulnerabilities.

secure_training.py & vulnerable_training.py
Training scripts used to demonstrate secure vs. insecure patterns.
