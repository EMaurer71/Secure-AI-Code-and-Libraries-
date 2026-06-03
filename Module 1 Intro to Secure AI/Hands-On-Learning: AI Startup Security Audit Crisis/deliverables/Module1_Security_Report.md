# Security Scan Results Report

## Executive Summary
This report summarizes the results of automated static analysis using Bandit, Semgrep, PyLint, and Safety on the ML training codebase. The goal is to identify hardcoded credentials, unsafe pickle operations, and exposed API keys, then prioritize remediation.

## Tool Summary
- Bandit findings: 11\n- Semgrep findings: 4\n- Safety vulnerabilities (raw entries): 8\n\n## Bandit Severity Breakdown

| severity   |   count |
|:-----------|--------:|
| LOW        |       9 |
| MEDIUM     |       2 |

## Bandit Findings by CWE

|   cwe |   0 |
|------:|----:|
|   259 |   1 |
|   502 |   4 |
|   703 |   6 |

## Semgrep Findings by Rule

| rule                                                     |   0 |
|:---------------------------------------------------------|----:|
| python.lang.security.deserialization.pickle.avoid-pickle |   4 |

## Top 10 Critical Vulnerabilities (Bandit-based)

|    | file                            |   line | test_id   |   cwe | severity   |   risk_score | text                                                                                                            |
|---:|:--------------------------------|-------:|:----------|------:|:-----------|-------------:|:----------------------------------------------------------------------------------------------------------------|
|  1 | supporting_files/demo_code_1.py |     51 | B301      |   502 | MEDIUM     |           13 | Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue. |
|  5 | supporting_files/demo_code_2.py |     79 | B301      |   502 | MEDIUM     |           13 | Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue. |
|  0 | supporting_files/demo_code_1.py |      8 | B403      |   502 | LOW        |           11 | Consider possible security implications associated with pickle module.                                          |
|  2 | supporting_files/demo_code_2.py |      8 | B403      |   502 | LOW        |           11 | Consider possible security implications associated with pickle module.                                          |
|  7 | supporting_files/demo_code_2.py |    133 | B105      |   259 | LOW        |            8 | Possible hardcoded password: 'MyP@ssw0rd123'                                                                    |
|  4 | supporting_files/demo_code_2.py |     43 | B101      |   703 | LOW        |            7 | Use of assert detected. The enclosed code will be removed when compiling to optimised byte code.                |
|  3 | supporting_files/demo_code_2.py |     42 | B101      |   703 | LOW        |            7 | Use of assert detected. The enclosed code will be removed when compiling to optimised byte code.                |
|  6 | supporting_files/demo_code_2.py |     96 | B101      |   703 | LOW        |            7 | Use of assert detected. The enclosed code will be removed when compiling to optimised byte code.                |
|  8 | supporting_files/demo_code_2.py |    151 | B101      |   703 | LOW        |            7 | Use of assert detected. The enclosed code will be removed when compiling to optimised byte code.                |
|  9 | supporting_files/demo_code_2.py |    152 | B101      |   703 | LOW        |            7 | Use of assert detected. The enclosed code will be removed when compiling to optimised byte code.                |

## Remediation Recommendations (High Level)
- Remove hardcoded credentials and move them to environment variables or secret managers.\n- Replace unsafe pickle deserialization with safer formats (e.g., JSON, ONNX, safetensors).\n- Add input validation and strict allowlists for file paths and external inputs.\n- Enforce automated scanning in CI/CD using GitHub Actions.\n