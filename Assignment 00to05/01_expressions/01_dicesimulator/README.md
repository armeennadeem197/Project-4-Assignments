# 🎲 Project 07: Dice Roll Simulator

## 📈 Overview
This Python program simulates rolling two six-sided dice three times and displays the result of each roll. It's designed to demonstrate how variable scope works in Python.

The project also includes enhancements such as a user-friendly welcome message, repeated simulations through loops, and input validation for a better user experience.

---

## 📚 Key Concepts Covered
- **Random number generation** using the `random` module
- **Function creation** and **variable scope**
- **Loops and control flow**
- **User input handling** and **validation**
- **Formatted output** with styling for clarity

---

## 💻 How It Works
1. The program starts with a styled welcome message.
2. It defines a function `roll_dice()` to roll two dice and print their total.
3. The `main()` function runs a loop to roll the dice three times.
4. A variable `die1` is declared in `main()` to illustrate local scope.
5. After completing three rolls, the program asks if the user wants to simulate again.
6. Input is validated to only accept "yes", "no", "y", or "n".

---

## 📊 Sample Output
```
==================================================
🎮 Welcome to the Dice Roll Simulator!
==================================================

🔧 Local die1 in main() starts as: 10

--- Roll 1 ---
🎲 Dice rolled: 2 + 5 = 7
--- Roll 2 ---
🎲 Dice rolled: 3 + 4 = 7
--- Roll 3 ---
🎲 Dice rolled: 1 + 6 = 7

🔧 Local die1 in main() ends as: 10

🔁 Do you want to roll again? (yes/no): no

👋 Thanks for using the Dice Roll Simulator! Goodbye!
```

---

## 📁 Files Included
- `main.py`: Main Python source code
- `README.md`: Documentation for the project

---

## 💡 How to Run the Program
Make sure you have Python 3 installed. Then run the file using:
```bash
python dice_simulator.py
```

---

## 👤 Author
**Name:** Amna Khalil  
**Project:** Dice Simulator  
---

Enjoy rolling your virtual dice! 🎲🎉

