# Program: Square Number Calculator
# Author: Amna Khalil
# Description: Asks the user for a number, calculates and displays its square,
#              includes input validation, looping, and styled messages.

from termcolor import colored

def get_valid_number(prompt: str) -> float:
    """Prompt user for a valid number with input validation."""
    while True:
        try:
            number = float(input(colored(prompt, "cyan")))
            return number
        except ValueError:
            print(colored("❌ Invalid input. Please enter a valid number!", "red"))

def main():
    print(colored("\n\t🔢🔢 Welcome to the Square Number Calculator 🔢🔢\n", "light_magenta", attrs=["bold"]))

    while True:
        num = get_valid_number("Type a number to see its square: ")
        squared = num ** 2
        print(colored(f"\n✅ {num} squared is {squared}\n", "yellow"))

        again = input(colored("🔁 Do you want to calculate another square? (yes/no): ", "light_blue")).strip().lower()
        if again not in ["yes", "y"]:
            print(colored("\n👋 Thank you for using the Square Number Calculator!", "green"))
            break

if __name__ == '__main__':
    main()
