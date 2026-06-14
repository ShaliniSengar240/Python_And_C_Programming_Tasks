# Predefined username and password
correct_username = "admin"
correct_password = "password123"

# Take input from the user
username = input("Enter Username: ")
password = input("Enter Password: ")

# Validate credentials
if username == correct_username and password == correct_password:
    print("Login Successful")
else:
    print("Invalid Username or Password")
