Why Secure AI Matters
This folder contains the first demonstration notebook from Module 1 — Intro to Secure AI Development in the Coursera course Secure AI Code & Libraries with Static Analysis.
It introduces the foundational idea that AI systems can be compromised even when the surrounding application code appears safe.

The demo focuses on understanding AI‑specific vulnerabilities, how they arise, and why traditional software security alone is not enough.

🎯 Learning Goals
This demonstration teaches you to:

Recognize AI‑specific attack vectors

Understand how model files can be weaponized

Identify insecure ML development patterns

See how static analysis can reveal hidden risks

Build intuition for secure AI development practices

These concepts form the base for the rest of the module and connect directly to the hands‑on lab.

📘 Notebook Included
AI Security Vulnerabilities Demo
File: AI_Security_Vulnerabilities_Demo.ipynb

This notebook walks through several real‑world examples of how AI systems can be compromised.

🔍 1. Understanding AI‑Specific Vulnerabilities
The demo covers:

Unsafe deserialization

Malicious model payloads

Data poisoning

Over‑permissive model APIs

Insecure preprocessing pipelines

You see how vulnerabilities can hide inside:

Model files

Preprocessing logic

Feature extraction

Third‑party libraries

🧪 2. Demonstrating a Malicious Model
The notebook uses:

Code
malicious_model.pkl
This file simulates a weaponized model artifact—a common real‑world attack where an attacker embeds malicious code inside a serialized model.

The demo shows:

How loading an untrusted model can execute arbitrary code

Why model provenance and integrity checks matter

How static analysis tools can detect unsafe loading patterns

🛡 3. Connecting to Secure AI Development
The notebook introduces the core principles of:

Model integrity

Supply‑chain security

Secure serialization

Safe model loading patterns

These concepts are reinforced later in:

The static analysis demo

The Module 1 hands‑on lab

The GitHub Actions security workflow

📁 Files in This Folder
AI_Security_Vulnerabilities_Demo.ipynb
A guided walkthrough of common AI security risks and how they manifest in real systems.

malicious_model.pkl
A deliberately unsafe model file used to demonstrate:

Arbitrary code execution

Unsafe deserialization

Why untrusted model artifacts are dangerous

This file is not harmful in this environment—it is a controlled teaching example.

🧠 Why This Demo Matters
This is the first moment in the course where you see that:

AI systems introduce new classes of vulnerabilities that traditional software security does not cover.

The demo sets the stage for:

Static analysis

Secure model handling

Dependency scanning

The full Module 1 security audit lab

CI/CD security automation

It’s the conceptual foundation for everything that follows.
