# Programming Task 04 - Functions, File Handling & Student Management System

## Intern Details

**Name:** Shalini Sengar  
**Date:** 14 June 2026

---

# Objective

The objective of this task is to understand and implement:

- Functions and Modular Programming
- Menu-Driven Programs
- Student Information Management
- Marks Analysis
- File Handling
- Password Vault Simulation
- Structured Programming in Python and C

---

# Programs Included

## Python Files

- calculator_functions.py
- student_manager.py
- marks_analyzer.py
- file_handling.py
- password_vault.py

## C Files

- calculator_functions.c
- student_manager.c
- marks_analyzer.c
- file_handling.c
- password_vault.c

---

# Program Descriptions

## 1. Calculator Functions

A menu-driven calculator program that performs basic arithmetic operations using separate functions.

### Operations

- Addition
- Subtraction
- Multiplication
- Division

### Sample Output

```text
1. Addition
2. Subtraction
3. Multiplication
4. Division

Enter Choice: 1
Enter First Number: 10
Enter Second Number: 20

Result: 30
```

---

## 2. Student Information Manager

This program accepts student details and displays them in a formatted manner using functions.

### Input

- Student Name
- Roll Number
- Branch
- Semester

### Sample Output

```text
Student Information

Name: Shalini Sengar
Roll No: 101
Branch: MCA
Semester: 3
```

---

## 3. Marks Analysis System

This program accepts marks for five subjects and calculates:

- Total Marks
- Percentage
- Grade

### Grade Criteria

| Percentage | Grade |
|------------|--------|
| 90 and Above | A |
| 80 - 89 | B |
| 70 - 79 | C |
| 60 - 69 | D |
| Below 60 | F |

### Sample Output

```text
Enter Marks of 5 Subjects:

Subject 1: 90
Subject 2: 85
Subject 3: 80
Subject 4: 88
Subject 5: 87

Total Marks: 430
Percentage: 86%

Grade: B
```

---

## 4. File Handling Program

This program creates a file named `student_data.txt`, stores student information, and then reads and displays the stored data.

### Stored Information

- Name
- Roll Number
- Branch
- Marks

### Sample Output

```text
Student Record Saved Successfully

Reading File...

Name: Shalini
Roll No: 101
Branch: MCA
Marks: 85
```

---

## 5. Password Vault Simulator

This program stores website credentials in a text file and displays all saved records.

### Stored Information

- Website Name
- Username
- Password

### Sample Output

```text
Website: Gmail
Username: user@gmail.com
Password: Test@123

Record Saved Successfully
```

### Display Output

```text
Saved Credentials

Website: Gmail
Username: user@gmail.com
Password: Test@123
```

> Note: This project is developed for educational purposes only. Passwords are stored without encryption.

---

# Explanation of Functions Used

## Calculator Functions

### addition(num1, num2)

Adds two numbers and returns the result.

### subtraction(num1, num2)

Subtracts the second number from the first number and returns the result.

### multiplication(num1, num2)

Multiplies two numbers and returns the result.

### division(num1, num2)

Divides the first number by the second number and returns the result.

---

## Student Information Manager Functions

### getStudentData()

Accepts student details such as name, roll number, branch, and semester from the user.

### displayStudentData()

Displays the entered student information in a formatted manner.

---

## Marks Analysis Functions

### calculateTotal()

Calculates the total marks obtained in all five subjects.

### calculatePercentage()

Calculates the percentage based on total marks.

### calculateGrade()

Determines the grade according to the percentage obtained.

### displayResult()

Displays total marks, percentage, and grade in a formatted manner.

---

## File Handling Functions

### writeData()

Creates a file and stores student information in it.

### readData()

Reads the stored data from the file and displays it.

---

## Password Vault Functions

### saveCredentials()

Stores website name, username, and password into a text file.

### displayCredentials()

Reads and displays all saved credentials from the file.

---

# Concepts Covered

- Functions
- Function Calls
- Arguments and Parameters
- Return Statements
- Modular Programming
- Menu-Driven Programming
- User Input Handling
- Conditional Statements
- File Handling
- Data Storage
- Structured Programming
- Basic Record Management

---

# Screenshots

Program execution screenshots are included in the **Screenshots** folder.

The screenshots contain:

- Calculator Program Output
- Student Manager Output
- Marks Analyzer Output
- File Handling Output
- Password Vault Output

---

# Conclusion

This task helped in understanding the practical implementation of functions, modular programming, file handling, and data management concepts in both Python and C. The programs demonstrate how structured code can be used to organize applications efficiently and improve code reusability.

---

