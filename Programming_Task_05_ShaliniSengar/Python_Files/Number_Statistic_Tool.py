# Number Statistics Tool

numbers = []

# Accept 10 numbers from the user
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Calculate statistics
largest = max(numbers)
smallest = min(numbers)
total = sum(numbers)
average = total / len(numbers)

even_count = 0
odd_count = 0

# Count even and odd numbers
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Display results
print("\nLargest Number:", largest)
print("Smallest Number:", smallest)
print("Sum:", total)
print("Average:", average)
print("Even Numbers:", even_count)
print("Odd Numbers:", odd_count)
