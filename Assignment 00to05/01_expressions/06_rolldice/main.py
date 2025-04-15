""# 🎲 Dice Roll Simulator

import os
import random
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Number of sides on each die
NUM_SIDES: int = 6

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def roll_dice() -> tuple[int, int, int]:
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    return die1, die2, total

def main():
    while True:
        clear_screen()
        print(Fore.YELLOW + Style.BRIGHT + """\
==========================================
       🎲 Welcome to Dice Roll Simulator 🎲
==========================================
Let's roll two dice and see what we get!
""")

        input(Fore.CYAN + "Press Enter to roll the dice...")

        die1, die2, total = roll_dice()

        print(Fore.MAGENTA + "\n---------------- Results ----------------")
        print(Fore.GREEN + f"Each die has {NUM_SIDES} sides.")
        print(Fore.BLUE + f"🎲 First Die: {die1}")
        print(Fore.BLUE + f"🎲 Second Die: {die2}")
        print(Fore.YELLOW + f"🔢 Total: {total}")
        print(Fore.MAGENTA + "------------------------------------------\n")

        again = input(Fore.CYAN + "Would you like to roll again? (yes/no): ").strip().lower()
        if again not in ('yes', 'y'):
            print(Fore.GREEN + "\nThanks for playing! 🎉\n")
            break

# Required to run the program
if __name__ == '__main__':
    main()
""
