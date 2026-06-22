# Student Marks Analyzer

marks = []

# Accept marks of 5 students
for i in range(5):
    mark = int(input(f"Enter marks of student {i + 1}: "))
    marks.append(mark)

# Calculate highest, lowest, and average marks
highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

# Display results
print("\nHighest Marks:", highest)
print("Lowest Marks:", lowest)
print("Average Marks:", average)
