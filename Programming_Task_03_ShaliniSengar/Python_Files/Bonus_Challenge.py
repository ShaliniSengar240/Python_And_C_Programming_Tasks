import random

# Generate a secret number between 1 and 50
secret_number = random.randint(1, 50)

attempts = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 50.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {secret_number}.")
        print(f"Number of attempts: {attempts}")
        break
