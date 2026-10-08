# 🔐 Secure OTP Generator

A simple cybersecurity project built using Python on Kali Linux.

This project generates a secure 6-digit OTP and provides OTP verification with security features such as expiry time, attempt limits, OTP hashing, activity logging, and security reporting.

## 🚀 Features

- 🔢 Secure 6-digit OTP generation
- ⏱️ 30-second OTP expiry
- 🚫 Maximum 3 verification attempts
- 🔄 OTP resend functionality
- 🔐 SHA-256 OTP hashing
- 📊 Security activity logging
- 📈 Security report
- 🛡️ Secure OTP generation using Python `secrets`

## 🛠️ Technologies Used

- Python 3
- Kali Linux
- SHA-256
- Python `secrets` module

## ▶️ How to Run

Clone the repository:

```bash
git clone <repository-url>
cd otp-generator

Run the program:
python3 otp_generator.py

🔒 Security

The OTP is generated using Python's secrets module.

The OTP is hashed using SHA-256 before verification.

The activity log does not store the actual OTP.

📊 Security Features

The program tracks:
  -OTP generation
  -Invalid attempts
  -Successful verification
  -Expired OTPs
  -OTP resends
  -Blocked verification attempts


👨‍💻 Author

Mohammed Nihal

Cybersecurity Student
