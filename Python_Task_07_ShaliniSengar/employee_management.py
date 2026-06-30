import csv

class Employee:
    def __init__(self, emp_id, name, department, designation, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.designation = designation
        self.salary = salary

employees = []

# Add Employee
def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    designation = input("Enter Designation: ")
    salary = float(input("Enter Salary: "))

    emp = Employee(emp_id, name, department, designation, salary)
    employees.append(emp)
    print("\nEmployee Added Successfully!\n")

# View Employees
def view_employees():
    if not employees:
        print("\nNo Employee Records Found!\n")
        return

    print("\n---------------------------------------------------------------")
    print("{:<10}{:<20}{:<15}{:<15}{:<10}".format(
        "ID", "Name", "Department", "Designation", "Salary"))
    print("---------------------------------------------------------------")

    for emp in employees:
        print("{:<10}{:<20}{:<15}{:<15}{:<10}".format(
            emp.emp_id,
            emp.name,
            emp.department,
            emp.designation,
            emp.salary))

# Search Employee
def search_employee():
    choice = input("Search by (1) ID or (2) Name: ")

    if choice == "1":
        emp_id = input("Enter Employee ID: ")
        for emp in employees:
            if emp.emp_id == emp_id:
                display_employee(emp)
                return

    elif choice == "2":
        name = input("Enter Employee Name: ").lower()
        for emp in employees:
            if emp.name.lower() == name:
                display_employee(emp)
                return

    print("\nEmployee Not Found!\n")

# Display Employee
def display_employee(emp):
    print("\nEmployee Details")
    print("----------------------------")
    print("ID:", emp.emp_id)
    print("Name:", emp.name)
    print("Department:", emp.department)
    print("Designation:", emp.designation)
    print("Salary:", emp.salary)

# Update Employee
def update_employee():
    emp_id = input("Enter Employee ID to Update: ")

    for emp in employees:
        if emp.emp_id == emp_id:
            emp.department = input("New Department: ")
            emp.designation = input("New Designation: ")
            emp.salary = float(input("New Salary: "))
            print("\nEmployee Updated Successfully!\n")
            return

    print("\nEmployee Not Found!\n")

# Delete Employee
def delete_employee():
    emp_id = input("Enter Employee ID to Delete: ")

    for emp in employees:
        if emp.emp_id == emp_id:
            employees.remove(emp)
            print("\nEmployee Deleted Successfully!\n")
            return

    print("\nEmployee Not Found!\n")

# Salary Statistics
def salary_statistics():
    if not employees:
        print("\nNo Employee Records Found!\n")
        return

    salaries = [emp.salary for emp in employees]

    print("\nSalary Statistics")
    print("-----------------------")
    print("Highest Salary :", max(salaries))
    print("Lowest Salary  :", min(salaries))
    print("Average Salary :", sum(salaries) / len(salaries))
    print("Total Employees:", len(employees))

# Export Data
def export_data():
    with open("employees.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["ID", "Name", "Department", "Designation", "Salary"])

        for emp in employees:
            writer.writerow([
                emp.emp_id,
                emp.name,
                emp.department,
                emp.designation,
                emp.salary
            ])

    print("\nData Exported Successfully to employees.csv\n")

# Read Data
def read_data():
    try:
        with open("employees.csv", "r") as file:
            reader = csv.reader(file)

            print("\nEmployee Records from CSV")
            print("--------------------------------")

            for row in reader:
                print(row)

    except FileNotFoundError:
        print("\nCSV File Not Found!\n")

# Main Menu
while True:
    print("\n========= Employee Management System =========")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Salary Statistics")
    print("7. Export Data")
    print("8. Read Data")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        update_employee()

    elif choice == "5":
        delete_employee()

    elif choice == "6":
        salary_statistics()

    elif choice == "7":
        export_data()

    elif choice == "8":
        read_data()

    elif choice == "9":
        print("\nThank You for Using Employee Management System!")
        break

    else:
        print("\nInvalid Choice! Please Try Again.")