# Input student details
name = input("Enter Name: ")
roll_no = int(input("Enter Roll Number: "))
branch = input("Enter Branch: ")
marks = int(input("Enter Marks: "))

# Write data to file
with open("student_data.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Roll No: {roll_no}\n")
    file.write(f"Branch: {branch}\n")
    file.write(f"Marks: {marks}\n")

print("\nStudent Record Saved Successfully")

# Read and display file contents
print("\nReading File...\n")

with open("student_data.txt", "r") as file:
    content = file.read()
    print(content)
