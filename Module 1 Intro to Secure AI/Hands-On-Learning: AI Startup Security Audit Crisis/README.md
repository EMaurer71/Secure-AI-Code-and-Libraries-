# Hands‑On Learning — AI Startup Security Audit Crisis  
### Based on Coursera: Secure AI Code & Libraries with Static Analysis

This hands‑on lab mirrors the Coursera scenario where you act as the AI security engineer responding to a real-world ML security incident.

You will perform a **static analysis–driven audit** of an AI startup’s codebase.

## 🎯 Learning Objectives
This lab teaches you how to:
- Apply static analysis tools to AI/ML code
- Identify insecure coding patterns in data pipelines and model loaders
- Detect unsafe serialization, path traversal, and hardcoded secrets
- Evaluate dependency and supply chain risks
- Produce a structured AI security assessment

## 📘 Notebook Included
### **ai_startup_security_audit_lab.ipynb**

This notebook walks through:

### 🔍 1. Running Static Analysis Tools (as taught in the Coursera module)
- Bandit → Python security issues  
- Semgrep → Pattern-based ML security rules  
- Safety → Dependency CVEs  
- Pylint → Code quality & error detection  

### 🧪 2. Reviewing ML Code for Vulnerabilities
You will analyze:
- Model loading logic  
- Data ingestion pipelines  
- API endpoints  
- Configuration and secrets  

### 🛠 3. Identifying AI‑Specific Risks
Including:
- Unsafe deserialization  
- Data poisoning vectors  
- Over-informative APIs  
- Hardcoded secrets  
- Supply chain vulnerabilities  

### 📝 4. Producing a Security Report
You will document:
- Findings  
- Severity  
- Impact  
- Recommended remediations  

## 🧠 Why This Lab Matters
This lab is the **practical application** of the Coursera module’s core message:

> *Static analysis reveals vulnerabilities that unit tests and runtime behavior never expose.*

This is your first real AI security audit.
