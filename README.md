# Blockchain Lab 2 – Decentralized Identity (DID) Certificate Verification

This project demonstrates how **Decentralized Identity (DID)** can be applied in education to issue and verify digital certificates securely.  

We simulate the following roles:  
- **University (Issuer):** Issues and signs certificates using cryptographic keys.  
- **Student (Holder):** Receives and stores the issued certificate.  
- **Employer (Verifier):** Verifies authenticity without contacting the university again.  

This reflects real-world use cases like **digital diplomas, driving licenses, passports, and KYC documents**.  

## Project Overview
- Certificates are issued and signed by a university using its private key.  
- The student stores both the certificate and the university’s public key.  
- Employers use the public key to verify authenticity.  
- If the certificate has been altered, verification will **fail immediately**.  

👉 DID ensures **trust without manual verification** from the issuer every time.  

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/blockchain-lab2.git
cd blockchain-lab2
```

### 2. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Install Dependencies
```bash
pip install cryptography
```
## Running the Project

### Step 1 – University Issues Certificate
```bash
python3 university_issue.py
```
### Step 2 – Student Stores Certificate
```bash
python3 student_holder.py
```
Student receives certificate and signature for safekeeping.
### Step 3 – Employer Verifies Certificate
```bash
python3 employer_verify.py
```
- Expected Output (Valid):
      - Employer verified: Certificate is valid and signed by University.
- Expected Output (Tampered):
      - Employer verification failed. Certificate may be forged.




