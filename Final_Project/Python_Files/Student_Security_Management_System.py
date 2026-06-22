students = []
security_scores = []


def add_student():
    name = input("Enter Student Name: ")
    sid = input("Enter Student ID: ")
    branch = input("Enter Branch: ")
    email = input("Enter Email Address: ")

    student = {
        "ID": sid,
        "Name": name,
        "Branch": branch,
        "Email": email
    }

    students.append(student)

    file = open("students.txt", "a")
    file.write(f"{sid},{name},{branch},{email}\n")
    file.close()

    print("Student added successfully.\n")


def view_students():
    if len(students) == 0:
        print("No records found.\n")
    else:
        for student in students:
            print("ID:", student["ID"])
            print("Name:", student["Name"])
            print("Branch:", student["Branch"])
            print("Email:", student["Email"])
            print()


def search_student():
    key = input("Enter Student Name or ID: ")

    found = False

    for student in students:
        if student["Name"] == key or student["ID"] == key:
            print(student)
            found = True

    if not found:
        print("Student not found.\n")


def delete_student():
    sid = input("Enter Student ID to delete: ")

    for student in students:
        if student["ID"] == sid:
            students.remove(student)
            print("Student deleted successfully.")
            return

    print("Record not found.")


def security_assessment():
    score = 0

    mfa = input("Is MFA Enabled (yes/no): ")
    password_length = int(input("Password Length: "))
    updated = input("System Updated (yes/no): ")
    antivirus = input("Antivirus Installed (yes/no): ")

    if mfa.lower() == "yes":
        score += 25

    if password_length >= 8:
        score += 25

    if updated.lower() == "yes":
        score += 25

    if antivirus.lower() == "yes":
        score += 25

    security_scores.append(score)

    if score >= 90:
        status = "Excellent"
    elif score >= 70:
        status = "Good"
    elif score >= 50:
        status = "Moderate"
    else:
        status = "Poor"

    print("Security Score:", score)
    print("Status:", status)


def generate_report():
    print("\n----- REPORT -----")
    print("Total Students:", len(students))

    if len(security_scores) > 0:
        average = sum(security_scores) / len(security_scores)
        print("Security Scores:", security_scores)
        print("Average Security Score:", average)

        print("Students with Poor Security Ratings:")
        for score in security_scores:
            if score < 50:
                print(score)
    else:
        print("No security assessment records available.")


# Cyber Security Feature 1
def password_strength_checker():
    password = input("Enter Password: ")

    if len(password) >= 8:
        print("Strong Password")
    else:
        print("Weak Password")


# Cyber Security Feature 2
def username_generator():
    name = input("Enter Name: ")
    birth_year = input("Enter Birth Year: ")

    username = name.lower() + birth_year
    print("Generated Username:", username)


# Cyber Security Feature 3
def login_validation():
    username = input("Username: ")
    password = input("Password: ")

    if username == "admin" and password == "admin123":
        print("Login Successful")
    else:
        print("Invalid Credentials")


while True:

    print("\n========================")
    print("Student Security Manager")
    print("========================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Security Assessment")
    print("6. Generate Report")
    print("7. Password Strength Checker")
    print("8. Username Generator")
    print("9. Login Validation")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        view_students()

    elif choice == 3:
        search_student()

    elif choice == 4:
        delete_student()

    elif choice == 5:
        security_assessment()

    elif choice == 6:
        generate_report()

    elif choice == 7:
        password_strength_checker()

    elif choice == 8:
        username_generator()

    elif choice == 9:
        login_validation()

    elif choice == 10:
        print("Thank You")
        break

    else:
        print("Invalid Choice")
