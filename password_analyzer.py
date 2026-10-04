import re
import random
import string
import hashlib

# Function to check password strength
def check_strength(password):
    strength = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        strength += 2
    else:
        feedback.append("Use at least 12 characters.")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Add uppercase letters.")

    # Lowercase check
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Add lowercase letters.")

    # Digit check
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Include numbers.")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Include special characters.")

    return strength, feedback

# Function to suggest a strong random password
def suggest_password(length=16):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

# Function to hash password (for reuse prevention)
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Example database of old passwords (hashed)
old_passwords = set()

# Main program
def main():
    password = input("Enter your password: ")
    strength, feedback = check_strength(password)

    print("\nPassword Strength Score:", strength, "/6")

    if strength <= 2:
        print("Classification: Weak")
    elif strength <= 4:
        print("Classification: Medium")
    else:
        print("Classification: Strong")

    if feedback:
        print("\nSuggestions to improve your password:")
        for f in feedback:
            print("-", f)

    # Suggest a strong alternative
    print("\nSuggested strong password:", suggest_password())

    # Check reuse
    hashed = hash_password(password)
    if hashed in old_passwords:
        print("\n⚠️ This password has been used before. Choose a new one.")
    else:
        old_passwords.add(hashed)
        print("\n✅ Password accepted and stored securely.")

if __name__ == "__main__":
    main()
