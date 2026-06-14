# Username Generator

# Taking user input
first_name = input("Enter your First Name: ").strip().lower()
last_name = input("Enter your Last Name: ").strip().lower()
birth_year = input("Enter your Birth Year: ").strip()

# Generate username suggestions
username1 = first_name + last_name + birth_year
username2 = first_name[0] + "." + last_name + birth_year[-2:]
username3 = last_name + "_" + first_name
username4 = first_name + "_" + birth_year
username5 = last_name + first_name[0] + birth_year
username6 = first_name + "." + last_name

# Display usernames
print("\nUsername Suggestions:")
print("1.", username1)
print("2.", username2)
print("3.", username3)
print("4.", username4)
print("5.", username5)
print("6.", username6)
