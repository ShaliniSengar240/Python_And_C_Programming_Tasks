marks = int(input("Enter your marks: "))

if marks >= 90 and marks <= 100:
    print("Grade: A")
elif marks >= 80 and marks <= 89:
    print("Grade: B")
elif marks >= 70 and marks <= 79:
    print("Grade: C")
elif marks >= 60 and marks <= 69:
    print("Grade: D")
elif marks >= 0 and marks < 60:
    print("Grade: F")
else:
    print("Invalid marks")
