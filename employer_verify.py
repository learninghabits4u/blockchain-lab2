"""
Employer (Verifier)
- Loads University public key
- Verifies certificate authenticity
"""

import json
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes

# Load University public key
with open("data/university_public.pem", "rb") as f:
    uni_public = serialization.load_pem_public_key(f.read())

# Load certificate
with open("data/certificate.json", "r") as f:
    certificate = json.load(f)

# Load signature
with open("data/signature.bin", "rb") as f:
    signature = f.read()

# Verify certificate
try:
    uni_public.verify(
        signature,
        str(certificate).encode(),
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )
    print("Employer verification successful. Certificate is authentic.")
except:
    print("Employer verification failed. Certificate may be forged.")
