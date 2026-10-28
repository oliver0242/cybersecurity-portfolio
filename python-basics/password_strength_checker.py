
import string

def check_password_strength(password):
    score = 0

    if len(password) >= 12:
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char in string.punctuation for char in password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Moderate"
    return "Strong"


if __name__ == "__main__":
    password = input("Enter a test password (do not use a real password): ")
    print("Estimated strength:", check_password_strength(password))
