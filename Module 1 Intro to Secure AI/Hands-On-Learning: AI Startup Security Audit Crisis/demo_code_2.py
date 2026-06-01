"""
Static Analysis Demonstration for AI Security
This file contains vulnerable code examples that PASS unit tests
but contain serious security issues caught by static analysis
"""

import pandas as pd
import pickle
import os
import numpy as np
from sklearn.linear_model import LogisticRegression

print("="*70)
print("STATIC ANALYSIS DEMONSTRATION")
print("Running code examples that pass tests but have security issues")
print("="*70)

# ============================================================================
# EXAMPLE 1: DATA LOADING WITHOUT VALIDATION
# ============================================================================

print("\n" + "="*70)
print("EXAMPLE 1: DATA LOADING FUNCTION")
print("="*70)

def load_training_data(file_path):
    """
    Loads training data from CSV file
    PASSES TESTS: Works correctly with valid inputs
    SECURITY ISSUES: No validation, size limits, or integrity checks
    """
    df = pd.read_csv(file_path)
    return df

# Unit test that PASSES
def test_load_training_data():
    """Test passes because it uses a small, trusted test file"""
    test_data = pd.DataFrame({'feature1': [1, 2, 3], 'label': [0, 1, 0]})
    test_data.to_csv('test_data.csv', index=False)
    
    result = load_training_data('test_data.csv')
    assert len(result) == 3
    assert 'feature1' in result.columns
    print("✓ Unit test PASSED")
    
    os.remove('test_data.csv')

print("\n[Running unit test...]")
test_load_training_data()

print("\n[What Static Analysis Would Flag:]")
print("⚠️  WARNING: No input validation on file_path parameter")
print("⚠️  WARNING: No file size limit checking")
print("⚠️  WARNING: No data integrity verification (checksums)")
print("⚠️  WARNING: No anomaly detection in loaded data")
print("⚠️  WARNING: Could load malicious/poisoned data in production")
print("\n🔍 Static analysis caught 5 security issues that tests missed!")


# ============================================================================
# EXAMPLE 2: MODEL LOADING WITH PATH TRAVERSAL
# ============================================================================

print("\n\n" + "="*70)
print("EXAMPLE 2: MODEL SERVING API")
print("="*70)

def load_and_predict(model_name, input_data):
    """
    Loads model and returns prediction
    PASSES TESTS: Works with valid model names
    SECURITY ISSUE: Path traversal vulnerability
    """
    # User-controlled input directly used in file path!
    model_path = f"models/{model_name}.pkl"
    
    # Load model (unsafe deserialization too!)
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    
    prediction = model.predict(input_data)
    return prediction

print("\n[Setting up test environment...]")
os.makedirs('models', exist_ok=True)
dummy_model = LogisticRegression()
dummy_model.fit(np.array([[1, 2], [3, 4]]), np.array([0, 1]))
with open('models/test_model.pkl', 'wb') as f:
    pickle.dump(dummy_model, f)

# Unit test that PASSES
def test_load_and_predict():
    """Test passes with legitimate model name"""
    input_data = np.array([[2, 3]])
    result = load_and_predict('test_model', input_data)
    assert len(result) == 1
    print("✓ Unit test PASSED")

print("\n[Running unit test...]")
test_load_and_predict()

print("\n[What Static Analysis Would Flag:]")
print("⚠️  CRITICAL: Unsanitized user input in file path")
print("⚠️  CRITICAL: Path traversal vulnerability")
print("    Attack example: model_name = '../../../etc/passwd'")
print("⚠️  CRITICAL: Unsafe pickle deserialization")
print("⚠️  WARNING: No authentication/authorization checks")
print("⚠️  WARNING: No rate limiting on model loading")
print("\n🔍 Static analysis caught 5 critical issues that tests missed!")

# Cleanup
os.remove('models/test_model.pkl')
os.rmdir('models')


# ============================================================================
# EXAMPLE 3: CONFIGURATION WITH HARDCODED SECRETS
# ============================================================================

print("\n\n" + "="*70)
print("EXAMPLE 3: CONFIGURATION MANAGEMENT")
print("="*70)

class ModelConfig:
    """
    Configuration for ML model deployment
    PASSES TESTS: Works correctly in test environment
    SECURITY ISSUES: Multiple secret management violations
    """
    def __init__(self):
        # ISSUE: Hardcoded credentials
        self.api_key = "sk-1234567890abcdef"
        self.db_password = "MyP@ssw0rd123"
        self.log_file = "/var/log/model.log"
        
    def get_credentials(self):
        """Returns credentials for external API"""
        # ISSUE: Logging sensitive information
        print(f"Using API key: {self.api_key}")
        return self.api_key
    
    def connect_database(self):
        """Connects to database"""
        connection_string = f"postgresql://user:{self.db_password}@localhost/mldb"
        return connection_string

# Unit test that PASSES
def test_config():
    """Test passes because credentials work in test environment"""
    config = ModelConfig()
    assert config.api_key is not None
    assert config.db_password is not None
    assert len(config.get_credentials()) > 0
    print("✓ Unit test PASSED")

print("\n[Running unit test...]")
test_config()

print("\n[What Static Analysis Would Flag:]")
print("⚠️  CRITICAL: Hardcoded API key in source code")
print("⚠️  CRITICAL: Hardcoded password in source code")
print("⚠️  CRITICAL: Sensitive data logged in plaintext")
print("⚠️  WARNING: No encryption for secrets at rest")
print("⚠️  WARNING: Password transmitted without encryption")
print("⚠️  WARNING: Credentials should be in environment variables")
print("\n🔍 Static analysis caught 6 security violations that tests missed!")


# ============================================================================
# SUMMARY
# ============================================================================

print("\n\n" + "="*70)
print("STATIC vs DYNAMIC ANALYSIS COMPARISON")
print("="*70)

print("\nAll three code examples:")
print("  ✓ Passed unit tests")
print("  ✓ Work correctly with test data")
print("  ✓ Would pass code review without security expertise")

print("\nBut static analysis found:")
print("  ⚠️  16 total security issues")
print("  ⚠️  8 critical vulnerabilities")
print("  ⚠️  100% invisible to runtime testing")

print("\nWhy runtime testing missed these:")
print("  • Tests use small, trusted datasets")
print("  • Tests use valid inputs only")
print("  • Tests use dummy credentials")
print("  • Tests check functionality, not security")

print("\nWhy static analysis caught them:")
print("  • Analyzes all possible code paths")
print("  • Checks for missing security controls")
print("  • Identifies dangerous patterns")
print("  • Validates secure coding standards")

print("\n" + "="*70)
print("KEY TAKEAWAY:")
print("Static analysis finds architectural security gaps that")
print("testing can't see—missing validations, unsafe patterns,")
print("and secrets that only appear in source code.")
print("="*70)