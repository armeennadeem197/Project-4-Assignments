import math
import os
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculate_hypotenuse(ab: float, ac: float) -> float:
    """
    Calculate the hypotenuse using the Pythagorean theorem.
    """
    return math.sqrt(ab ** 2 + ac ** 2)

def main():
    while True:
        clear_screen()
        print(Fore.CYAN + Style.BRIGHT + """
============================================
       🌟 Welcome to the Pythagorean Calculator 🌟
============================================
This tool calculates the hypotenuse (BC) of a right triangle
using the famous Pythagorean Theorem: BC² = AB² + AC²
        """)

        try:
            ab: float = float(input(Fore.YELLOW + "Enter the length of AB: "))
            ac: float = float(input(Fore.YELLOW + "Enter the length of AC: "))

            if ab <= 0 or ac <= 0:
                print(Fore.RED + "\n❌ Please enter positive values for both sides.")
                input("Press Enter to try again...")
                continue

        except ValueError:
            print(Fore.RED + "\n❌ Invalid input. Please enter numeric values only.")
            input("Press Enter to try again...")
            continue

        bc = calculate_hypotenuse(ab, ac)

        print(Fore.GREEN + "\n---------------- Calculation ----------------")
        print(Fore.GREEN + f"AB = {ab}")
        print(Fore.GREEN + f"AC = {ac}")
        print(Fore.GREEN + f"BC (hypotenuse) = √(AB² + AC²) = {bc:.2f}")
        print(Fore.GREEN + "---------------------------------------------\n")

        again = input(Fore.CYAN + "Would you like to calculate another hypotenuse? (yes/no): ").strip().lower()
        if again not in ('yes', 'y'):
            print(Fore.MAGENTA + "\nThanks for using the Pythagorean Calculator! 🎉")
            break

if __name__ == '__main__':
    main()
