Best Practices for AI Supply Chain Security
Module 3 — Secure AI Code & Libraries with Static Analysis
This module demonstrates end‑to‑end AI supply chain security using real-world practices adopted by modern ML/AI engineering teams. It includes:

Deterministic builds with lock files

SBOM generation (CycloneDX)

Dependency approval workflows

Automated CI/CD security gates

Organizational governance for ML supply chain security

This repository contains a polished Jupyter notebook implementing all five best practices in a clean, reproducible format.

🔐 1. Overview
Modern AI systems depend on dozens of third‑party libraries. Without proper controls, these dependencies introduce risks:

Vulnerabilities (CVEs)

Malicious packages (typosquatting)

License conflicts

Version drift

Supply chain attacks

This module shows how to secure the entire ML dependency lifecycle using industry‑standard tools and policies.

📁 2. Repository Contents
File	Purpose
Best_Practices_Supply_Chain.ipynb	Main notebook implementing all 5 practices
requirements.in	High‑level dependency input file
requirements.lock	Fully pinned lock file (41 packages)
sbom.json	CycloneDX SBOM for the ML pipeline
approval_policy.json	Dependency approval workflow rules
security_gate_config.json	CI/CD security gate configuration
organizational_policy.md	Full ML supply chain security policy


🧩 3. What the Notebook Covers
Practice 1 — Lock Files for Deterministic Builds
Uses pip-compile to generate a pinned requirements.lock

Ensures reproducible builds across all environments

Adds hash verification (--require-hashes)

Produces a dependency tree with 41 packages

Practice 2 — Software Bill of Materials (SBOM)
Generates a CycloneDX 1.4 SBOM (sbom.json)

Includes component metadata, versions, purls, licenses, hashes

Enables fast CVE impact analysis

Supports compliance (HIPAA, FDA, NTIA minimum elements)

Practice 3 — Dependency Approval Workflows
Defines rules for:

ML frameworks (torch, tensorflow, jax)

Restrictive licenses (GPL/AGPL)

New/unknown publishers

High‑risk categories (crypto, network, subprocess)

Includes SLAs and reviewer responsibilities

Practice 4 — Automated Security Gates
CI/CD pipeline enforces:

pip-audit + Safety vulnerability scanning

License compliance (pip-licenses)

Dependency approval checks

SBOM generation

Blocks merges on CRITICAL/HIGH vulnerabilities

Practice 5 — Organizational Policies
Full ML supply chain governance:

Lock files required

SBOMs required for every release

Vulnerability SLAs (24h/7d/30d/90d)

Quarterly audits

Roles & responsibilities

🛠️ 4. Tools Used
pip-tools — lock file generation

CycloneDX — SBOM generation

pip-audit — vulnerability scanning

Safety — extended CVE scanning

pip-licenses — license compliance

Python 3.9+

🚀 5. How to Use This Notebook
Open the notebook in Jupyter or VS Code

Run each section sequentially

Generated artifacts will appear in the working directory:

requirements.lock

sbom.json

approval_policy.json

security_gate_config.json

organizational_policy.md

These files can be used as templates for real ML projects.

🧠 6. Why This Matters
AI supply chain security is now a regulatory requirement in healthcare, finance, and government. This module demonstrates:

How to prevent dependency‑based attacks

How to enforce security automatically

How to maintain compliance with SBOM‑based workflows

How to build reproducible, auditable ML systems
