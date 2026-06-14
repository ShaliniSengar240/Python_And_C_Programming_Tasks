n = int(input("Enter a number: "))

sum_numbers = 0
even_count = 0
odd_count = 0

for i in range(1, n + 1):
    sum_numbers += i

    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Sum of numbers from 1 to", n, "=", sum_numbers)
print("Count of even numbers =", even_count)
print("Count of odd numbers =", odd_count)
