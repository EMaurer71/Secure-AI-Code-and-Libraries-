Hands‑On Learning — AI Startup Security Audit Crisis
It explains the two notebooks, the workflow, the deliverables, and the purpose of the lab.
It fits perfectly into:

Code
Module 1 Intro to Secure AI Development/
└── Hands-On-Learning: AI Startup Security Audit Crisis/README.md
All key concepts include Guided Links so you can expand the repo later.

Hands‑On Learning — AI Startup Security Audit Crisis
This folder contains the fully reconstructed and enhanced hands‑on lab from the Coursera course:

Secure AI Code & Libraries with Static Analysis

In this scenario, you act as the AI security engineer responding to a real‑world ML security incident at a fictional startup.
Your task is to perform a static analysis–driven audit of their AI codebase, identify vulnerabilities, and produce a structured security report.

This lab originally shipped with no instructions and only partial scan outputs.
I rebuilt the entire environment, added missing files, and created a complete GitHub Actions demonstration to make the lab fully reproducible and engineering‑ready.

🎯 Learning Objectives
This lab teaches you how to:

Apply static analysis tools to AI/ML code

Identify insecure coding patterns in data pipelines and model loaders

Detect unsafe serialization, path traversal, and hardcoded secrets

Evaluate dependency and supply‑chain risks

Produce a structured AI security assessment

Automate scans using GitHub Actions

These skills form the foundation of secure AI development and are reinforced throughout the course.

📘 Included Notebooks
1. AI Startup Security Audit Lab
File: notebooks/ai_startup_security_audit_lab.ipynb

This notebook walks through the full static analysis workflow:

🔍 Static Analysis Tools
You run the same tools introduced in the Coursera demonstrations:

Bandit — Python security issues

Semgrep — Pattern‑based ML security rules

Safety — Dependency CVEs

PyLint — Code quality & error detection

🧪 Code Review for ML Vulnerabilities
You analyze:

Model loading logic

Data ingestion pipelines

API endpoints

Configuration and secrets

🛠 AI‑Specific Risks Identified
Including:

Unsafe deserialization

Data poisoning vectors

Over‑informative APIs

Hardcoded secrets

Supply‑chain vulnerabilities

📝 Security Report Creation
You produce:

Findings

Severity

Impact

Recommended remediations

This notebook is the core of the lab and mirrors the real‑world workflow of an AI security engineer.

2. GitHub Actions Security Demo
File: notebooks/github_actions_security_demo.ipynb

This notebook demonstrates how to automate the entire audit using GitHub Actions.

It explains:

How the workflow triggers

How each tool runs in CI

How artifacts are uploaded

How to interpret CI logs

How to integrate static analysis into PR reviews

This notebook pairs with the workflow file in:

Code
.github/workflows/security_scan.yaml
Together, they show how to build a continuous AI security pipeline.

📂 Folder Structure
Code
Hands-On-Learning: AI Startup Security Audit Crisis/
├── .github/workflows/
│   └── security_scan.yaml
│
├── deliverables/
│   ├── Module1_Security_Report.md
│   └── remediation_matrix.csv
│
├── notebooks/
│   ├── ai_startup_security_audit_lab.ipynb
│   └── github_actions_security_demo.ipynb
│
├── security-reports/
│   ├── bandit-results.json
│   ├── pylint-results.txt
│   ├── safety-results.json
│   └── semgrep-results.json
│
└── supporting_files/
    ├── demo_code_1.py
    └── demo_code_2.py
📁 Supporting Files
supporting_files/demo_code_1.py & demo_code_2.py
Intentionally vulnerable Python scripts used to generate realistic static analysis findings.

These include examples of:

Unsafe file handling

Hardcoded secrets

Insecure model loading

Missing input validation

They are the “target codebase” for your audit.

📁 Security Reports
The security-reports/ folder contains the raw outputs from each tool:

bandit-results.json

pylint-results.txt

safety-results.json

semgrep-results.json

These feed into the final deliverables.

📁 Deliverables
Module1_Security_Report.md
A structured AI security assessment summarizing:

Findings

Severity

Impact

Recommendations

remediation_matrix.csv
A prioritized list of fixes, mapped to:

CWE categories

Risk levels

Affected components

Both were recreated based on the scan results and assignment requirements.
