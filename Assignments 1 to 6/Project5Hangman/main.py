import random

HANGMAN_STAGES = [
    """
    +---+
    |   |
        |
        |
        |
        |
    =========""",
    """
    +---+
    |   |
    O   |
        |
        |
        |
    =========""",
    """
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========""",
    """
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========""",
    """
    +---+
    |   |
    O   |
   /|\\  |
        |
        |
    =========""",
    """
    +---+
    |   |
    O   |
   /|\\  |
   /    |
        |
    =========""",
    """
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
    ========="""
]

def choose_word():
    """Select a random word from categories"""
    word_categories = {
        "Programming": ["python", "javascript", "algorithm", "function", "variable"],
        "Animals": ["elephant", "giraffe", "kangaroo", "dolphin", "rhinoceros"],
        "Countries": ["canada", "brazil", "japan", "australia", "germany"]
    }
    category = random.choice(list(word_categories.keys()))
    return random.choice(word_categories[category]), category

def display_word(word, guessed_letters):
    """Display the word with guessed letters revealed"""
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    """Main game function"""
    word, category = choose_word()
    guessed_letters = set()
    incorrect_guesses = []
    attempts_left = 6
    
    print("\n" + "="*40)
    print("🎩 Welcome to Hangman! 💀".center(40))
    print(f"Category: {category}".center(40))
    print("="*40)
    print(HANGMAN_STAGES[0])
    
    while attempts_left > 0:
        print("\nWord:", display_word(word, guessed_letters))
        print("Incorrect guesses:", ", ".join(incorrect_guesses))
        print(f"Attempts left: {attempts_left}")
        
        guess = input("\nGuess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter!")
            continue
            
        if guess in guessed_letters or guess in incorrect_guesses:
            print("You already guessed that letter!")
            continue
            
        if guess in word:
            guessed_letters.add(guess)
            print("✅ Correct guess!")
        else:
            incorrect_guesses.append(guess)
            attempts_left -= 1
            print("❌ Wrong guess!")
            print(HANGMAN_STAGES[6 - attempts_left])
        
        if set(word) == guessed_letters:
            print("\n" + "="*40)
            print("🎉 Congratulations! You guessed the word:".center(40))
            print(word.upper().center(40))
            print("="*40)
            return
    
    print("\n" + "="*40)
    print("💀 Game Over! The word was:".center(40))
    print(word.upper().center(40))
    print("="*40)

def main():
    while True:
        hangman()
        play_again = input("\nWould you like to play again? (y/n): ").lower()
        if play_again != 'y':
            print("\nThanks for playing! Goodbye! 👋")
            break

if __name__ == "__main__":
    main()