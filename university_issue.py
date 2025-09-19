
"""
University (Issuer)
- Generates DID (keys)
- Issues signed certificate
- Shares public key with Student & Employer
"""

import json
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# Generate University key pair (DID)
uni_private = rsa.generate_private_key(public_exponent=65537, key_size=2048)
uni_public = uni_private.public_key()

# Save public key so others can verify later
with open("data/university_public.pem", "wb") as f:
    f.write(uni_public.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))

# Create a student certificate
certificate = {
    "name": "Alice",
    "degree": "B.Tech Computer Science",
    "year": "2025"
}

# Sign the certificate
signature = uni_private.sign(
    str(certificate).encode(),
    padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
    hashes.SHA256()
)

# Save certificate + signature
with open("data/certificate.json", "w") as f:
    json.dump(certificate, f, indent=2)

with open("data/signature.bin", "wb") as f:
    f.write(signature)

print("University issued certificate and stored data in 'data/' folder.")

