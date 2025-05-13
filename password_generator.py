import random
import string

def generate_password(length=12, use_symbols=True):
    # Base character set
    chars = string.ascii_letters + string.digits
    if use_symbols:
        chars += string.punctuation

    # Randomly choose characters
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# ---- Main interaction ----
print("🔐 Python Password Generator 🔐")
length = int(input("Enter password length: "))
symbols = input("Include symbols? (y/n): ").lower().startswith("y")

password = generate_password(length, symbols)
print(f"\nGenerated password: {password}")