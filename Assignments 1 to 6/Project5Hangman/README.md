# 🎩 Hangman - Guess the Word! 💀

## 🌟 Features

- 🎮 Fun and classic Hangman gameplay.
- 🧠 Tests your vocabulary and word-guessing skills.
- 🔤 Letter-by-letter guessing.
- 🖼️ Visual feedback with Hangman stages.
- 🚫 Tracks incorrect guesses and remaining attempts.
- 📂 Word selection from categorized lists (Programming, Animals, Countries).
- 🌍 Random category and word selection for each game.
- ✅ Clear indication of correct guesses.
- ❌ Feedback on incorrect guesses.
- 🏆 Congratulatory message upon winning.
- 😭 Game over message revealing the secret word.
- 🔄 Option to play multiple rounds.

## 🎮 How to Play

1.  The computer will randomly select a secret word from one of the categories (Programming, Animals, or Countries).
2.  The category of the word will be displayed.
3.  The secret word is initially shown as a series of underscores (`_`), representing the unguessed letters.
4.  You need to guess one letter at a time.
5.  Enter your letter guess in the prompt.
6.  **Correct Guess:** If your letter is in the secret word, all occurrences of that letter will be revealed.
7.  **Incorrect Guess:** If your letter is not in the secret word, it will be added to the list of incorrect guesses, and one attempt will be deducted. The Hangman figure will also progress to the next stage.
8.  You have a limited number of attempts (6). The game ends if:
    -   You correctly guess all the letters in the word before running out of attempts. **You win!** 🎉
    -   You run out of attempts before guessing the word. **Game Over!** 💀 The secret word will be revealed.
9.  After each game, you'll be asked if you want to play again.

## 📋 Example Gameplay

Markdown

# 🎩 Hangman - Guess the Word! 💀

## 🌟 Features

- 🎮 Fun and classic Hangman gameplay.
- 🧠 Tests your vocabulary and word-guessing skills.
- 🔤 Letter-by-letter guessing.
- 🖼️ Visual feedback with Hangman stages.
- 🚫 Tracks incorrect guesses and remaining attempts.
- 📂 Word selection from categorized lists (Programming, Animals, Countries).
- 🌍 Random category and word selection for each game.
- ✅ Clear indication of correct guesses.
- ❌ Feedback on incorrect guesses.
- 🏆 Congratulatory message upon winning.
- 😭 Game over message revealing the secret word.
- 🔄 Option to play multiple rounds.

## 🎮 How to Play

1.  The computer will randomly select a secret word from one of the categories (Programming, Animals, or Countries).
2.  The category of the word will be displayed.
3.  The secret word is initially shown as a series of underscores (`_`), representing the unguessed letters.
4.  You need to guess one letter at a time.
5.  Enter your letter guess in the prompt.
6.  **Correct Guess:** If your letter is in the secret word, all occurrences of that letter will be revealed.
7.  **Incorrect Guess:** If your letter is not in the secret word, it will be added to the list of incorrect guesses, and one attempt will be deducted. The Hangman figure will also progress to the next stage.
8.  You have a limited number of attempts (6). The game ends if:
    -   You correctly guess all the letters in the word before running out of attempts. **You win!** 🎉
    -   You run out of attempts before guessing the word. **Game Over!** 💀 The secret word will be revealed.
9.  After each game, you'll be asked if you want to play again.

## 📋 Example Gameplay

======================================== 🎩 Welcome to Hangman! 💀 Category: Animals

+---+
|   |
    |
    |
    |
    |
=========

Word: _ _ _ _ _ _ _ _ _
Incorrect guesses:
Attempts left: 6

Guess a letter: e
✅ Correct guess!

Word: _ _ _ _ _ _ _ _ e
Incorrect guesses:
Attempts left: 6

Guess a letter: l
✅ Correct guess!

Word: _ _ _ _ _ _ _ l e
Incorrect guesses:
Attempts left: 6

Guess a letter: p
✅ Correct guess!

Word: _ _ _ p _ _ _ l e
Incorrect guesses:
Attempts left: 6

Guess a letter: h
❌ Wrong guess!
+---+
|   |
O   |
|
|
|
=========

Word: _ _ _ p _ _ _ l e
Incorrect guesses: h
Attempts left: 5

... (game continues) ...

Guess a letter: a
✅ Correct guess!

======================================== 🎉 Congratulations! You guessed the word: KANGAROO
Would you like to play again? (y/n): n

Thanks for playing! Goodbye! 👋


## ⚙️ How to Run the Game

1.  Make sure you have **Python 3** installed on your system.
2.  Save the provided Python code as a `.py` file (e.g., `hangman.py`).
3.  Open your terminal or command prompt.
4.  Navigate to the directory where you saved the file.
5.  Run the game by executing the command: `python hangman.py`
6.  Follow the on-screen instructions to play!

## 📌 Learning Outcomes

This project demonstrates several important programming concepts:

-   **🐍 Python Fundamentals:** Variables, data structures (lists, dictionaries, sets), loops (`while`), conditional statements (`if`, `else`, `elif`), functions.
-   **🎲 Randomness:** Using the `random` module to select words and categories.
-   **🔤 String Manipulation:** Working with strings to display the word and check for letter occurrences.
-   **👤 User Input:** Getting input from the user using the `input()` function.
-   **🖼️ List Indexing:** Using list indexing to display the appropriate Hangman stage.
-   **🧠 Game Logic:** Implementing the rules and flow of the Hangman game.
-   **✨ User Experience:** Providing clear feedback and a user-friendly interface.

Enjoy playing Hangman and testing your word knowledge! 😊