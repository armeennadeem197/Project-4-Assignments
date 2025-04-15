import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0
    guess = None

    print("🔢 Welcome to the Number Guessing Game!")
    print("🎯 I've picked a number between 1 and 100.")
    print("Can you guess what it is? Let's find out!\n")

    while guess != secret_number:
        try:
            guess = int(input("👉 Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("📉 Too low! Try again.\n")
            elif guess > secret_number:
                print("📈 Too high! Try again.\n")
        except ValueError:
            print("⚠️ Invalid input! Please enter a valid number.\n")

    print(f"🎉 Congratulations! You guessed it right: {secret_number}")
    print(f"🧠 Total attempts: {attempts}")
    print("Thanks for playing! 🙌")

guess_the_number()
