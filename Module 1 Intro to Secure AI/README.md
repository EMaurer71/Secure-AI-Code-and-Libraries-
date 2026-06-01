# Module 1 — Intro to Secure AI Development  
### Based on Coursera: Secure AI Code & Libraries with Static Analysis

This module introduces the foundational security mindset required for modern AI development.  
It aligns with the Coursera module that explains **why AI systems fail in unique ways** and why secure coding practices matter before you ever train or deploy a model.

## 🎯 Learning Objectives
This module helps you understand:
- Why AI systems introduce new classes of vulnerabilities
- How insecure model formats, data pipelines, and APIs create attack surfaces
- Why traditional software testing is insufficient for AI systems
- How static analysis complements AI development workflows

## 📘 Notebook Included
### **AI_Security_Vulnerabilities_Demo.ipynb**
This notebook demonstrates the three core vulnerability classes highlighted in the Coursera module:

1. **Arbitrary Code Execution via Pickle**  
   - Mirrors the course’s warning about unsafe serialization formats  
   - Shows how loading a malicious model can execute attacker code  

2. **Data Poisoning Attacks**  
   - Demonstrates how unvalidated data pipelines can corrupt model behavior  
   - Reinforces the course’s emphasis on data integrity  

3. **Model Extraction Attacks**  
   - Shows how over-informative APIs leak model internals  
   - Connects to the course’s discussion of model confidentiality risks  

## 🧠 Why This Module Matters
This module sets the stage for:
- Static analysis  
- Secure coding standards  
- Safe model formats  
- Data validation  
- API hardening  
- Supply chain security  

It provides the **threat awareness** needed before learning the tools.
R
