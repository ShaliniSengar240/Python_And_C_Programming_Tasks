# Take password input from the user
password = input("Enter Password: ")

# Check conditions
has_length = len(password) >= 8
has_number = any(char.isdigit() for char in password)
has_uppercase = any(char.isupper() for char in password)

# Determine password strength
if has_length and has_number and has_uppercase:
    print("Strong Password")
elif has_length and (has_number or has_uppercase):
    print("Moderate Password")
else:
    print("Weak Password")
