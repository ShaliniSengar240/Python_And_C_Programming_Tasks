# Function to display student information

def display_student(name, roll_no, branch, semester):
    print("\nStudent Information")
    print("-------------------")
    print("Name      :", name)
    print("Roll No   :", roll_no)
    print("Branch    :", branch)
    print("Semester  :", semester)

# Taking input from user
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")
branch = input("Enter Branch: ")
semester = input("Enter Semester: ")

# Function call
display_student(name, roll_no, branch, semester)
