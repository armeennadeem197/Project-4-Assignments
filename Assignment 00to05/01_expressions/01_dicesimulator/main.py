"""
Program: dice_simulator.py
Author: Armeen Nadeem
----------------------
This program simulates rolling two dice three times.
It demonstrates how variable scope works in Python.

Features:
- Random dice rolls
- Repeated execution with user interaction
- Styled welcome message
"""

import random

NUM_SIDES = 6  # Number of sides on each die

def roll_dice():
    """Simulates rolling two dice and prints their total."""
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    total: int = die1 + die2
    print(f"🎲 Dice rolled: {die1} + {die2} = {total}")

def main():
    print("="*50)
    print("🎮 Welcome to the Dice Roll Simulator!".center(50))
    print("="*50)

    while True:
        die1: int = 10  # Local variable for scope demonstration
        print(f"\n🔧 Local die1 in main() starts as: {die1}\n")
        
        for i in range(3):
            print(f"--- Roll {i+1} ---")
            roll_dice()

        print(f"\n🔧 Local die1 in main() ends as: {die1}")

        again = input("\n🔁 Do you want to roll again? (yes/no): ").strip().lower()
        while again not in ['yes', 'y', 'no', 'n']:
            again = input("❗ Please enter 'yes' or 'no': ").strip().lower()
        if again in ['no', 'n']:
            print("\n👋 Thanks for using the Dice Roll Simulator! Goodbye!")
            break


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
