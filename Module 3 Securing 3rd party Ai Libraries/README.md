README #1 — Module 3: Securing 3rd‑Party AI Libraries
Location:
Module 3 Securing 3rd party Ai Libraries/README.md

Module 3 — Securing 3rd‑Party AI Libraries
This module contains my reconstructed and expanded work for Module 3 of the Coursera course “Secure AI Code & Libraries with Static Analysis.”  
The focus of this module is understanding and mitigating risks introduced by third‑party AI/ML libraries, including:

Vulnerable dependencies

Unsafe model loading utilities

Supply‑chain attacks

License compliance issues

SBOM generation and analysis

CI/CD security gates for ML pipelines

Module 3 includes two classroom demonstrations and two hands‑on labs, all rebuilt and enhanced to be fully runnable and portfolio‑ready.

📘 Classroom Demo 1 — Third‑Party Library Risks in AI
Folder:
Third-Party Library Risks in AI/

This demo introduces:

Dependency vulnerabilities

Model loader risks

Unsafe serialization

**Organizational policy enforcement****

Library approval workflows

Notebook:
module_3_third_party_library_risks.ipynb

Supporting files include:

approval_policy.json

organizational_policy.md

Multiple requirements files for PyTorch, TensorFlow, and scikit‑learn

📙 Classroom Demo 2 — Tools for Dependency & License Analysis
Folder:
Tools for Dependency & License Analysis/

This demo shows how to use:

Bandit

Semgrep

PyLint

pip‑audit

Safety

pip‑licenses

CycloneDX SBOM generation

Notebook:
module_3_tools_dependency_license_analysis.ipynb

Includes:

Vulnerable requirements file

SBOM example

Security gate configuration

Before/after scan reports

🧪 Lab 1 — Project Secure Healthcare ML Pipeline
Folder:
Project Secure Healthcare ML Pipeline/

This is the capstone lab for Module 3.
You perform a full dependency and supply‑chain security audit of a healthcare ML pipeline.

Includes:

Multiple reconstructed notebooks

A complete GitHub Actions workflow

Before/after scan reports

A full security report

A reflection document

Vulnerable and fixed model loader code

🧪 Lab 2 — Healthcare AI Supply Chain Breach Response
Folder:
Healthcare AI Supply Chain Breach Response/

This lab simulates a real‑world supply‑chain breach in a healthcare AI system.
You perform:

Dependency audits

SBOM analysis

Snyk scanning

Policy enforcement

Multi‑stage remediation

Includes:

Multiple reconstructed notebooks

Audit results

Deliverable reports

Dependency monitoring policy

🧠 Why This Module Matters
Third‑party libraries are the largest attack surface in modern AI systems.
This module teaches you how to:

Detect vulnerable dependencies

Enforce organizational policies

Generate and analyze SBOMs

Build CI/CD security gates

Respond to supply‑chain breaches

These skills are essential for secure AI development in production environments.
