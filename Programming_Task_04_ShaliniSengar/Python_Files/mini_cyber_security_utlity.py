website = input("Enter Website Name: ")
username = input("Enter Username: ")
password = input("Enter Password: ")

# Save data to file
with open("vault.txt", "a") as file:
    file.write(f"Website: {website}\n")
    file.write(f"Username: {username}\n")
    file.write(f"Password: {password}\n\n")

print("\nRecord Saved Successfully!")

# Display all saved records
print("\n--- Saved Records ---\n")

with open("vault.txt", "r") as file:
    print(file.read())
