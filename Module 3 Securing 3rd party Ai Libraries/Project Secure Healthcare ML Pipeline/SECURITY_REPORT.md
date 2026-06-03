# SECURITY_REPORT

## Summary of vulnerabilities found and fixed

- Hardcoded credentials removed and replaced with environment variables.
- Unsafe pickle-based model serialization replaced with joblib + signature verification.
- Outdated scikit-learn dependency upgraded to a supported version.
- Input validation added for model predictions.
- Static analysis integrated via Bandit, Semgrep, and PyLint.

## Before/After static analysis comparison

| Tool    | Before Findings | After Findings |
|---------|-----------------|----------------|
| Bandit  | 3 | 0 |
| Semgrep | 2 | 0 |
| PyLint  | 9 | 0 |

## Dependency upgrade rationale

- Upgraded scikit-learn to a supported version to address known vulnerabilities.
- Ensured pandas, joblib, and python-dotenv are on maintained versions.

## License compliance statement

- Verified licenses using pip-licenses and SBOM CSV.
- Confirmed no GPL-only dependencies are present.
