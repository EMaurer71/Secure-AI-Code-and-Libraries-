# What Is Static Analysis?  
### Based on Coursera: Secure AI Code & Libraries with Static Analysis

This module explains the role of **static analysis** in securing AI systems.  
It aligns with the Coursera module that teaches how static analysis finds vulnerabilities that functional tests never reveal.

## 🎯 Learning Objectives
You will learn:
- What static analysis is and how it works
- Why AI/ML code contains unique security risks
- How static analysis detects structural vulnerabilities
- Why unit tests cannot catch missing validation or unsafe patterns

## 📘 Notebook Included
### **AI_Static_Analysis_Demo.ipynb**

This notebook demonstrates three examples of code that:
- Pass unit tests  
- Work correctly with valid inputs  
- Still contain serious security vulnerabilities  

These examples directly reflect the Coursera module’s teaching goals.

### 🧪 Example 1 — Data Loading Without Validation
Static analysis flags:
- Missing input validation  
- Missing file size limits  
- Missing integrity checks  
- Potential for poisoned or malicious data  

### 🧪 Example 2 — Path Traversal + Unsafe Pickle Deserialization
Static analysis detects:
- User-controlled file paths  
- Path traversal patterns  
- Unsafe deserialization  
- Missing authentication and rate limiting  

### 🧪 Example 3 — Hardcoded Secrets
Static analysis identifies:
- API keys in source code  
- Passwords in connection strings  
- Sensitive data logged in plaintext  

## 🧠 Why This Module Matters
Static analysis is the **first line of defense** in secure AI development.  
It enforces secure coding standards before models are trained or deployed.

This module prepares you for:
- The hands-on audit lab  
- Writing secure ML code  
- Understanding AI-specific vulnerability patterns  
