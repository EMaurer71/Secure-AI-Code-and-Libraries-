README #2 — Third‑Party Library Risks in AI
Location:
Third-Party Library Risks in AI/README.md

Third‑Party Library Risks in AI
This folder contains the first classroom demonstration for Module 3 — Securing 3rd‑Party AI Libraries.
It introduces the risks associated with using external AI/ML libraries and shows how to evaluate them using organizational policies and dependency analysis.

📘 Notebook Included
Third‑Party Library Risks in AI
File: module_3_third_party_library_risks.ipynb

This notebook covers:

🔍 1. Dependency Risk Analysis
Vulnerable ML libraries

Unsafe model utilities

Deprecated APIs

Hidden transitive dependencies

📜 2. Organizational Policy Enforcement
Using:

approval_policy.json

organizational_policy.md

You evaluate whether a library is:

Approved

Restricted

Blocked

📦 3. Requirements File Comparison
You analyze:

PyTorch

TensorFlow

scikit‑learn

Secure baseline requirements

📁 Supporting Files
approval_policy.json

organizational_policy.md

requirements_pytorch.txt

requirements_tensorflow.txt

requirements_sklearn.txt

requirements_secure.txt

🧠 Why This Demo Matters
Most AI vulnerabilities originate from third‑party libraries, not your own code.
This demo teaches you how to:

Evaluate dependency risks

Enforce security policies

Build safer ML environments

It sets the stage for the full Module 3 labs.
