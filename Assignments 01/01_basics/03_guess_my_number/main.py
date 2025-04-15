import random

def main():
    # Generate the secret number at random!
    secret_number: int = random.randint(1, 99)
    
    print("I am thinking of a number between 1 and 99...")
    
    while True:
        try:
            # Get user's guess and convert to integer
            guess = int(input("Enter a guess: "))
            
            # If guess is not equal to secret number
            while guess != secret_number:
                if guess < secret_number:
                    print("Your guess is too low.")
                else:
                    print("Your guess is too high.")
                
                print()  # Print an empty line to tidy up the console
                guess = int(input("Enter a new guess: "))  # Get a new guess from the user

            # When the guess is correct
            print(f"Congrats! The number was: {secret_number}")
            break

        except ValueError:
            # Handle the case where the input is not a valid integer
            print("Please enter a valid number.")

if __name__ == '__main__':
    main()
