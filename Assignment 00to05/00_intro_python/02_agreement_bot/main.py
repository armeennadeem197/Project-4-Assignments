"""
Program: favorite_animal
------------------------
A fun Python program that asks the user for their favorite animal
and responds with a cheerful message using their input.
Created by: Amna Khalil
"""

from termcolor import colored
import re

def is_valid_animal_name(name):
    """Validates that the input only contains letters and optional spaces."""
    return bool(re.fullmatch(r"[A-Za-z ]+", name))

def main():
    print(colored("\n\t\t🐾 Welcome to the Favorite Animal Program 🐾\n", "light_magenta"))
    print(colored("\t\t    Created by: Amna Khalil\n", "cyan"))

    while True:
        favorite = input(colored("\nWhat's your favorite animal? ", "light_cyan")).strip()

        if not favorite:
            print(colored("❌ You didn't enter anything. Please type a valid animal name.", "red"))
            continue

        if not is_valid_animal_name(favorite):
            print(colored("❌ Invalid input! Please only use letters and spaces.", "red"))
            continue

        print(colored(f"\nMy favorite animal is also {favorite}! 🐶\n", "yellow"))

        repeat = input(colored("\nWould you like to try again? (yes/no): ", "light_green")).strip().lower()
        if repeat not in ["yes", "y"]:
            print(colored("\n\t\tThanks for sharing your favorite! 🐾\n", "light_magenta"))
            break


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
