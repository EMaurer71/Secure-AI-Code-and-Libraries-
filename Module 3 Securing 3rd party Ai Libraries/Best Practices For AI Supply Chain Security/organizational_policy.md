
# ML Supply Chain Security Policy v1.0

## 1. Dependency Management

1.1 All production ML systems MUST use lock files
    • Tool: pip-tools (requirements.lock)
    • Hash verification REQUIRED
    • Monthly dependency review

1.2 All dependencies MUST be approved before use
    • See approval_policy.json for rules
    • Exceptions require CISO approval

1.3 Dependency updates MUST be tested before deployment
    • Run full test suite
    • Performance regression tests
    • Security scan

## 2. Software Bill of Materials (SBOM)

2.1 SBOM MUST be generated for every release
    • Format: CycloneDX 1.4+
    • Stored in central SBOM repository
    • Retained for 3 years

2.2 SBOMs MUST be queryable for vulnerability management
    • Daily automated CVE checks
    • Alert affected teams within 4 hours

## 3. Vulnerability Management

3.1 Vulnerability SLAs by Severity:
    • CRITICAL: Patch within 24 hours
    • HIGH: Patch within 7 days
    • MEDIUM: Patch within 30 days
    • LOW: Patch within 90 days

3.2 Zero-day vulnerabilities
    • Immediate incident response
    • Assess impact using SBOMs
    • Emergency patching process

## 4. CI/CD Security Gates

4.1 All code changes MUST pass security gates
    • Vulnerability scanning (pip-audit + Safety)
    • License compliance check
    • Dependency approval verification

4.2 No exceptions without security team approval
    • Document justification
    • Time-limited exceptions only

## 5. Third-Party Package Vetting

5.1 New packages MUST be vetted before approval
    • Security review for high-risk packages
    • License compatibility check
    • Maintainer reputation assessment
    • Age and adoption metrics

5.2 Approved package list maintained by security team
    • Reviewed quarterly
    • Deprecated packages removed

## 6. Roles and Responsibilities

6.1 Data Scientists / ML Engineers
    • Request approval for new dependencies
    • Update dependencies per vulnerability SLAs
    • Generate SBOMs for releases

6.2 Security Team
    • Review and approve dependency requests
    • Maintain security policies
    • Monitor CVE feeds and alert teams
    • Audit compliance quarterly

6.3 Platform Team
    • Maintain CI/CD security gates
    • Operate SBOM repository
    • Provide tooling and automation

## 7. Metrics and Compliance

7.1 Track and report monthly:
    • % of systems with current SBOMs
    • Vulnerability SLA compliance rate
    • Average time to patch by severity
    • Number of policy violations

7.2 Quarterly security review
    • Policy effectiveness
    • Tool updates
    • Process improvements
