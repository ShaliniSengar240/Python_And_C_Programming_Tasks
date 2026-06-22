# Employee Record Search

# Store employee names in a list
employees = ["John", "Alice", "David", "Sophia", "Michael"]

# Ask the user to enter a name to search
search_name = input("Enter employee name to search: ")

# Variable to check if record is found
found = False

# Search using a loop
for employee in employees:
    if employee.lower() == search_name.lower():
        found = True
        break

# Display result
if found:
    print("Record Found")
else:
    print("Record Not Found")
