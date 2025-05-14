import random
import string

def evaluate_strength(password):
    length = len(password)
    has_symbol = any(c in string.punctuation for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)

    if length >= 12 and has_symbol and has_upper and has_digit:
        return "Strong"
    elif length >= 8 and (has_upper or has_symbol):
        return "Moderate"
    else:
        return "Weak"

def generate_password(length=12, use_symbols=True):
    # Base character set
    chars = string.ascii_letters + string.digits
    if use_symbols:
        chars += string.punctuation

    # Randomly choose characters
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# ---- Main interaction ----
print("Python Password Generator")
length = int(input("Enter password length: "))
symbols = input("Include symbols? (y/n): ").lower().startswith("y")

password = generate_password(length, symbols)
print(f"\nGenerated password: {password}")
print(f"Strength: {evaluate_strength(password)}")
