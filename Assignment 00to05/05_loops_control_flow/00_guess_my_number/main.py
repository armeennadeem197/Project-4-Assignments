import random

def main():
    while True:
        secret_number = random.randint(1, 99)
        guess_count = 0  # Track the number of guesses
        max_attempts = 10  # Limit the number of attempts
        
        print("I am thinking of a number between 1 and 99... You have 10 attempts to guess it.")
        
        while guess_count < max_attempts:
            try:
                guess = int(input(f"Attempt {guess_count + 1}/{max_attempts} - Enter a guess: "))
                guess_count += 1  # Increment guess count

                if guess < secret_number:
                    print("Your guess is too low. Try a higher number.")
                elif guess > secret_number:
                    print("Your guess is too high. Try a lower number.")
                else:
                    print(f"🎉 Congrats! The number was {secret_number}. You guessed it in {guess_count} attempts!")
                    break  # Exit loop when guessed correctly
            except ValueError:
                print("Invalid input! Please enter a valid number.")

            # Give a hint after each guess
            if guess_count < max_attempts:
                print(f"You've got {max_attempts - guess_count} attempts left.")
        else:
            # Player ran out of attempts
            print(f"Sorry, you couldn't guess the number. It was {secret_number}.")
        
        # Ask the player if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == '__main__':
    main()
