# Day 5 - Number Guessing Game

import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Start guessing loop
while True:
    guess = input("Guess a number between 1 and 10: ")

    # Validate input
    if not guess.isdigit():
        print("❌ Please enter a valid number.")
        continue

    guess = int(guess)

    if guess < secret_number:
        print("🔼 Too low! Try again.")
    elif guess > secret_number:
        print("🔽 Too high! Try again.")
    else:
        print("🎉 Correct! You guessed the number.")
        break

