Module 1 — Intro to Secure AI Development

This module contains my reconstructed and expanded work for Module 1 of the Coursera course “Secure AI Code & Libraries with Static Analysis.” 

It includes the two class demonstration notebooks, the malicious model example, and the full hands‑on lab, which I rebuilt and enhanced due to missing instructions and incomplete artifacts in the original course materials.

This module now provides a complete, engineering‑ready introduction to:

AI security fundamentals

Common AI/ML vulnerabilities

Static analysis tools for AI code

Automated security scanning with GitHub Actions

Generating security reports and remediation matrices

📘 Included Demonstrations
Why Secure AI Matters
Folder:
Why Secure AI Matters/

This demonstration notebook introduces:

Real‑world AI security failures

Common ML attack vectors

How insecure model handling leads to compromise

A malicious model example (malicious_model.pkl)

How to detect unsafe deserialization and model tampering

This notebook was enhanced to include clearer examples and additional context around model integrity risks.

What is Static Analysis
Folder:
What is Static Analysis/

This notebook demonstrates:

How static analysis applies to AI/ML code

Bandit, Semgrep, and PyLint basics

How to interpret findings

How static analysis complements dynamic testing

The original notebook was incomplete; I rebuilt missing cells and added examples to make the demonstration reproducible.

📙 Hands‑On Lab — AI Startup Security Audit Crisis
Folder:
Hands-On-Learning: AI Startup Security Audit Crisis/

The original Coursera lab provided only partial instructions and expected students to infer the workflow from scan results. I reconstructed the entire lab environment, added missing files, and built a complete GitHub Actions demonstration.

This lab now includes:

📁 supporting_files/
demo_code_1.py

demo_code_2.py  
Two intentionally vulnerable Python scripts used for static analysis.

📁 notebooks/
ai_startup_security_audit_lab.ipynb

Rebuilt from scratch

Runs Bandit, Semgrep, PyLint, and Safety

Generates security reports

Produces a remediation matrix

github_actions_security_demo.ipynb

Demonstrates how GitHub Actions runs the same scans automatically

Shows workflow triggers, logs, and artifact uploads

Explains CI/CD integration for AI security

📁 .github/workflows/
security_scan.yaml

Automated CI pipeline

Runs Bandit, Semgrep, PyLint, and Safety

Uploads scan results as artifacts

Mirrors the notebook’s local workflow

📁 security-reports/
Contains the output of the static analysis tools:

bandit-results.json

pylint-results.txt

safety-results.json

semgrep-results.json

📁 deliverables/
Module1_Security_Report.md

remediation_matrix.csv

These deliverables were recreated based on the scan results and assignment requirements.

📂 Folder Structure
Code
Module 1 Intro to Secure AI Development/
├── Why Secure AI Matters/
│   ├── AI_Security_Vulnerabilities_Demo.ipynb
│   └── malicious_model.pkl
│
├── What is Static Analysis/
│   ├── AI_Static_analysis_Demo.ipynb
│   └── README.md
│
└── Hands-On-Learning: AI Startup Security Audit Crisis/
    ├── .github/workflows/security_scan.yaml
    ├── deliverables/
    ├── notebooks/
    ├── security-reports/
    ├── supporting_files/
    └── README.md
Why This Module Was Recreated
The original course materials were missing:

Instructions for the hands‑on lab

Required files for static analysis

GitHub Actions workflow

Security report templates

Remediation matrix structure

Notebook outputs and code cells

I rebuilt the entire module using:

The scan results

The assignment prompts

The expected deliverables

My own enhancements to improve clarity and reproducibility

This module now provides a complete, professional, and fully runnable introduction to secure AI development.ovides the **threat awareness** needed before learning the tools.
R
