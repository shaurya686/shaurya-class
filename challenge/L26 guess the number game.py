import random

# Step 1: Let the computer pick a number between 1 and 100
secret_number = random.randint(1, 100)

# Step 2: Let the user guess until they get it right
guess = None
tries = 0

print("🎯 I'm thinking of a number between 1 and 100. Can you guess it?")

while guess != secret_number:
    guess = int(input("Enter your guess: "))
    tries += 1

    if guess < secret_number:
        print("🔼 Too low!")
    elif guess > secret_number:
        print("🔽 Too high!")
    else:
        print(f"🎉 You got it! The number was {secret_number}.")
        print(f"📊 It took you {tries} tries.")
