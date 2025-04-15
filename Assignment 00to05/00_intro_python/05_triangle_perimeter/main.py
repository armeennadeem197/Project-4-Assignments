# 📁 Project 05: Triangle Perimeter Calculator
# 👩‍💼 Author: Amna Khalil
# 🗓️ Date: April 2025
# 🔍 Description: Prompts user for triangle side lengths, validates inputs, and calculates the perimeter with styled output.

from termcolor import colored

def get_valid_float(prompt: str) -> float:
    """Prompt the user until they provide a valid float number."""
    while True:
        try:
            value = float(input(colored(prompt, "cyan")))
            if value <= 0:
                print(colored("❌ Please enter a positive number!", "red"))
            else:
                return value
        except ValueError:
            print(colored("❌ Invalid input! Please enter a numeric value.", "red"))

def main():
    print(colored("\n\t 🔺🔺 Welcome to the Triangle Perimeter Calculator 🔺🔺\n", "light_magenta", attrs=["bold"]))

    while True:
        side1 = get_valid_float("Enter the length of side 1: ")
        side2 = get_valid_float("Enter the length of side 2: ")
        side3 = get_valid_float("Enter the length of side 3: ")

        perimeter = side1 + side2 + side3
        print(colored(f"\n✅ The perimeter of the triangle is {perimeter:.2f}\n", "yellow"))

        again = input(colored("🔁 Do you want to calculate another perimeter? (yes/no): ", "light_blue")).strip().lower()
        if again not in ["yes", "y"]:
            print(colored("\n👋 Thank you for using the Triangle Perimeter Calculator!", "green"))
            break

if __name__ == '__main__':
    main()
