import secrets
import time
import sys
import select
import hashlib
from datetime import datetime

print("=" * 45)
print("          SECURE OTP GENERATOR")
print("=" * 45)

total_generated = 0
invalid_attempts = 0
successful_verifications = 0
expired_otps = 0
resend_count = 0
blocked_count = 0


def generate_otp():
    return str(secrets.randbelow(900000) + 100000)


def hash_otp(otp):
    return hashlib.sha256(otp.encode()).hexdigest()


def log_event(message):
    with open("otp_activity.log", "a") as log:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"[{timestamp}] {message}\n")


def show_report():
    print("\n" + "=" * 45)
    print("             SECURITY REPORT")
    print("=" * 45)
    print(f"OTP Generated          : {total_generated}")
    print(f"Invalid Attempts       : {invalid_attempts}")
    print(f"Successful Verification: {successful_verifications}")
    print(f"Expired OTPs           : {expired_otps}")
    print(f"OTP Resends            : {resend_count}")
    print(f"Blocked Verifications  : {blocked_count}")
    print("=" * 45)


while True:

    otp = generate_otp()
    otp_hash = hash_otp(otp)

    total_generated += 1
    log_event("OTP generated")

    expiry_time = time.time() + 30
    attempts = 0
    max_attempts = 3

    print("\nYour OTP is:", otp)
    print("OTP is valid for 30 seconds")

    while attempts < max_attempts:

        remaining = int(expiry_time - time.time())

        if remaining <= 0:
            print("\nOTP Expired!")
            expired_otps += 1
            log_event("OTP expired")

            choice = input("Resend OTP? (y/n): ").strip().lower()

            if choice == "y":
                resend_count += 1
                log_event("OTP resent")
                print("Generating new OTP...")
                break
            else:
                log_event("Verification cancelled")
                show_report()
                sys.exit()

        print(
            f"\rTime remaining: {remaining:2d} seconds | "
            f"Attempt {attempts + 1}/3 | Enter OTP: ",
            end=""
        )
        sys.stdout.flush()

        ready, _, _ = select.select([sys.stdin], [], [], 1)

        if ready:
            user_otp = sys.stdin.readline().strip()

            if time.time() > expiry_time:
                print("\nOTP Expired!")
                expired_otps += 1
                log_event("OTP expired")

                choice = input("Resend OTP? (y/n): ").strip().lower()

                if choice == "y":
                    resend_count += 1
                    log_event("OTP resent")
                    print("Generating new OTP...")
                    break
                else:
                    show_report()
                    sys.exit()

            attempts += 1

            user_hash = hash_otp(user_otp)

            if user_hash == otp_hash:
                print("\nOTP Verified Successfully!")
                successful_verifications += 1
                log_event("OTP verification successful")

                show_report()
                sys.exit()

            else:
                invalid_attempts += 1
                print(f"\nInvalid OTP! Attempt {attempts}/3")
                log_event(f"Invalid OTP attempt {attempts}")

    else:
        print("\nMaximum attempts reached!")
        print("OTP verification blocked.")

        blocked_count += 1
        log_event("Maximum attempts reached - verification blocked")

        show_report()
        sys.exit()
