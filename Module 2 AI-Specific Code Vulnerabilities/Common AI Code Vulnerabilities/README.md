README — Common AI Code Vulnerabilities
Location:
Module 2 AI-Specific Code Vulnerabilities/Common AI Code Vulnerabilities/README.md

Common AI Code Vulnerabilities
This folder contains the classroom walkthrough portion of Module 2 — AI‑Specific Code Vulnerabilities from the Coursera course Secure AI Code & Libraries with Static Analysis.
These notebooks demonstrate the most common security weaknesses found in real AI/ML codebases and show how they can be exploited.

Each notebook focuses on a single vulnerability category and includes runnable examples, reconstructed code, and enhanced explanations.

🎯 Learning Objectives
This section teaches you to:

Recognize AI‑specific coding vulnerabilities

Understand how insecure ML code leads to compromise

Identify unsafe patterns in model loading, data pipelines, and dependencies

Build intuition for secure AI development

Prepare for static analysis and the hands‑on lab

These vulnerabilities form the foundation for the Static Analysis in Practice section.

📘 Included Notebooks
1. Insecure Pickle Deserialization
File: 01_insecure_pickle_deserialization.ipynb  
Shows how loading untrusted model files can lead to arbitrary code execution.

2. Hardcoded Credentials
File: 02_hardcoded_credentials.ipynb  
Demonstrates how secrets leak into ML pipelines and training scripts.

3. Path Traversal in Model Loading
File: 03_path_traversal_model_loading.ipynb  
Explains how user‑controlled paths can compromise model integrity.

4. Unsafe Data Pipelines
File: 04_unsafe_data_pipeline.ipynb  
Shows how unvalidated data flows can lead to poisoning or corruption.

5. Dependency Confusion
File: 05_dependency_confusion.ipynb  
Demonstrates how ML environments are vulnerable to malicious package injection.

🧠 Why This Section Matters
These notebooks introduce the core vulnerabilities that static analysis tools detect in the next part of the module.
They prepare you for:

Writing custom Semgrep rules

Scanning ML pipelines

Auditing real AI codebases

Completing the financial ML security audit lab

This section is the conceptual foundation for the rest of Module 2.
