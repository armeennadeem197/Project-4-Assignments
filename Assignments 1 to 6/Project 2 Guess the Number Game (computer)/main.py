import random
import time

def number_guessing_game():
    """
    A game where the computer tries to guess the user's number between 1-10.
    The user provides feedback if the guess is too high, too low, or correct.
    """
    
    print("\n" + "="*50)
    print("🤖 NUMBER GUESSING GAME 🤖".center(50))
    print("="*50)
    print("\nThink of a secret number between 1 and 10.")
    print("I'll try to guess it with your help!\n")
    
    # Game setup
    low = 1
    high = 10
    attempts = 0
    guess_history = []
    
    time.sleep(1)  # Pause for dramatic effect
    
    while True:
        # Computer makes a guess
        guess = random.randint(low, high)
        attempts += 1
        guess_history.append(guess)
        
        print(f"\n🔮 My guess #{attempts}: {guess}")
        
        # Get user feedback with validation
        while True:
            feedback = input("Is this too (H)igh, too (L)ow, or (C)orrect? ").lower()
            if feedback in ['h', 'l', 'c']:
                break
            print("Please enter H, L, or C!")
        
        # Process feedback
        if feedback == 'c':
            print(f"\n🎉 I guessed your number {guess} in {attempts} attempts!")
            print("My guesses:", " → ".join(map(str, guess_history)))
            break
        elif feedback == 'h':
            high = guess - 1
            print("Okay, I'll guess lower next time! ⬇️")
        else:
            low = guess + 1
            print("Okay, I'll guess higher next time! ⬆️")
        
        # Check if user is cheating
        if low > high:
            print("\n🤨 Hey! You changed your number, didn't you? Game over!")
            return
    
    # Play again option
    if input("\nWant to play again? (y/n): ").lower() == 'y':
        number_guessing_game()
    else:
        print("\nThanks for playing! Goodbye! 👋")

# Start the game
if __name__ == "__main__":
    number_guessing_game()