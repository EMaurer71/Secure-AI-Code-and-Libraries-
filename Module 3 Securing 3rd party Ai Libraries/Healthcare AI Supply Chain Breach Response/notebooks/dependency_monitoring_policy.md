# MedAI Dependency Monitoring Policy

## 1. Approval Workflow for New Packages

All new third-party dependencies must undergo a formal approval process before being
added to requirements.txt or Pipfile:

1. Developer Request: Developer submits a pull request adding the dependency, including justification.
2. Automated Scan: CI/CD pipeline automatically runs pip-audit and pip-licenses.
   - The build fails if vulnerabilities (CVSS > 4.0) or blacklisted licenses are detected.
3. Security Review: A security engineer reviews the package for typosquatting risks,
   maintainer reputation, and project activity.
4. Approval: Upon approval, the package version is strictly pinned (e.g., package==1.2.3)
   and hashes are added to the lockfile.

## 2. Update Schedule by Severity

- CRITICAL (CVSS 9.0 - 10.0): Patch and deploy within 24 hours.
- HIGH (CVSS 7.0 - 8.9): Patch and deploy within 7 days.
- MEDIUM (CVSS 4.0 - 6.9): Patch and deploy within 30 days.
- LOW (CVSS 0.1 - 3.9): Patch during the next scheduled maintenance window.

## 3. License Whitelist and Blacklist

- Whitelist (Approved for Commercial Use): MIT, Apache 2.0, BSD (2-Clause, 3-Clause), ISC.
- Blacklist (Prohibited): GPL (v2, v3), AGPL, SSPL, any license with "NonCommercial" clauses, UNKNOWN licenses.

## 4. SBOM Update Procedures

The Software Bill of Materials (SBOM) must be automatically regenerated using
cyclonedx-bom during every CI/CD build. The updated SBOM must be cryptographically
signed and stored in the artifact repository alongside the application container image. A copy
must be retained for 6 years to comply with HIPAA audit requirements.

## 5. Incident Response Plan for Supply Chain Attacks

In the event of a suspected supply chain compromise (e.g., detection of a typosquatted
package or compromised maintainer account):

1. Containment: Immediately isolate the affected training or production environments
   from the network to prevent data exfiltration.
2. Identification: Identify the malicious package, its entry point, and the extent of its
   execution using audit logs and the SBOM.
3. Eradication: Remove the malicious package, purge all compromised container
   images, and rotate all credentials, API keys, and access tokens present in the affected
   environment.
4. Recovery: Rebuild the environment from a known-good state using verified lockfiles
   and hashes.
5. Notification: Notify the legal and compliance teams immediately to initiate HIPAA
   breach notification protocols if Protected Health Information (PHI) was exposed.
