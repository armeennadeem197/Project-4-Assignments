# Remainder & Quotient Calculator

import os
from colorama import Fore, Style, init

# Initialize colorama for Windows
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_valid_input(prompt: str) -> int:
    while True:
        try:
            value = int(input(Fore.YELLOW + prompt + Style.RESET_ALL))
            return value
        except ValueError:
            print(Fore.RED + "\n❌ Invalid input! Please enter an integer." + Style.RESET_ALL)

def main():
    while True:
        clear_screen()
        print(Fore.CYAN + Style.BRIGHT + """
=========================================
       ➗ Remainder & Quotient Calculator
=========================================
Let's perform some division magic! ✨
        """ + Style.RESET_ALL)

        dividend = get_valid_input("Enter the dividend (number to divide): ")

        while True:
            divisor = get_valid_input("Enter the divisor (number to divide by): ")
            if divisor == 0:
                print(Fore.RED + "\n❌ Divisor cannot be zero! Try again." + Style.RESET_ALL)
            else:
                break

        quotient = dividend // divisor
        remainder = dividend % divisor

        print(Fore.GREEN + f"\n✅ The result of {dividend} divided by {divisor} is:")
        print(Fore.MAGENTA + f"Quotient: {quotient}")
        print(Fore.BLUE + f"Remainder: {remainder}\n")

        again = input(Fore.YELLOW + "Do you want to try another division? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print(Fore.CYAN + "\nThanks for using the Remainder & Quotient Calculator! 👋")
            break

if __name__ == '__main__':
    main()
