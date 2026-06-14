marks = []
total = 0

print("Enter marks for 5 subjects:")

for i in range(5):
    mark = int(input(f"Subject {i+1}: "))
    marks.append(mark)
    total += mark

percentage = total / 5

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
else:
    grade = "F"

print("\n----- Result -----")
print("Total Marks =", total)
print("Percentage =", round(percentage, 2), "%")
print("Grade =", grade)
