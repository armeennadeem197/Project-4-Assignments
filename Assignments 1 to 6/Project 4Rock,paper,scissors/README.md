✊✋✌️ Rock, Paper, Scissors Game

Welcome to the Rock, Paper, Scissors game! 🎮 This is a fun, interactive Python game 
where you can play against the computer. Whether you're a beginner or just looking for
 a quick game, this is the perfect way to pass some time!

 🌟 Features
🖥️ Play Rock, Paper, Scissors against the computer.

📊 Tracks the score for both the player and the computer.

🧑‍🤝‍🧑 User-friendly interface with easy prompts and responses.

🔄 Play as many rounds as you like or quit the game anytime.

✋ Simple and fast-paced gameplay with clear instructions.

⚡ Option to play with shortcuts: r for rock, p for paper, s for scissors.


🎮 How to Play
The game will prompt you to choose one of the following:

Rock, Paper, or Scissors.

You can use the shortcuts: r for Rock, p for Paper, and s for Scissors.

Once you make a selection, the computer will randomly choose its own move.

The game will then determine the winner based on the classic rules:

Rock beats Scissors ✊ > ✂️

Scissors beats Paper ✂️ > 📄

Paper beats Rock 📄 > ✊

The result of each round will be displayed, and the game will keep track of your score.

To quit the game at any time, simply type q or quit.

==============================
 🪨📄✂️ ROCK-PAPER-SCISSORS ✂️📄🪨 
==============================
Choose rock, paper, or scissors (or 'q' to quit): rock

You chose: Rock
Computer chose: Paper
Computer wins! 😢

Score - You: 0 | Computer: 1

Choose rock, paper, or scissors (or 'q' to quit): s

You chose: Scissors
Computer chose: Scissors
It's a tie! 🤝

Score - You: 0 | Computer: 1

Choose rock, paper, or scissors (or 'q' to quit): p

You chose: Paper
Computer chose: Rock
You win! 🎉

Score - You: 1 | Computer: 1

Choose rock, paper, or scissors (or 'q' to quit): q

Thanks for playing! Final Scores:
You: 1 | Computer: 1
Goodbye! 👋

📜 Code Overview
1. Choice Enum:
The game uses an Enum to represent the three possible choices: Rock, Paper, and Scissors. This makes the code more organized and readable.

2. get_user_choice Function:
This function is responsible for getting input from the player. It ensures that the user enters a valid choice and handles the case where they wish to quit the game.

3. determine_winner Function:
This function compares the user's and the computer's choices and determines the winner based on the classic game rules.

4. Main Game Loop:
The game runs in a loop, prompting the player for their choice, selecting the computer's choice, determining the winner, and displaying the updated score.

The loop continues until the player decides to quit by typing q.

🔄 Game Flow

Start the Game: The user is prompted to enter their choice.
Computer Makes a Choice: The computer randomly picks one of the options.
Determine Winner: Based on the choices, the game announces the result (win, lose, or tie).
Display Score: After each round, the score is displayed.
Quit or Continue: The player can choose to play another round or quit by typing q.

🤝 Contributing
Feel free to fork this repository, submit issues, or create pull requests. Contributions are welcome!
Ideas for Improvements:
Add more advanced features like a best of three mode or AI difficulty levels.
Enhance the graphics or interface using a Python GUI library like Tkinter.