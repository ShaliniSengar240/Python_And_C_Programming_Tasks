password = "admin123"
attempts = 0

while attempts < 3:
    user_password = input("Enter Password: ")

    if user_password == password:
        print("Access Granted")
        break
    else:
        attempts += 1
        print("Incorrect Password")

if attempts == 3:
    print("Account Locked")
