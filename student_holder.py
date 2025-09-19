"""
Student (Holder)
- Simply stores the certificate and signature
- Can present them to Employer for verification
"""

import json

# Load certificate issued by University
with open("data/certificate.json", "r") as f:
    certificate = json.load(f)

print("Student received certificate:")
print(json.dumps(certificate, indent=2))
print("\n(Student keeps signature.bin and can share with Employer)")
