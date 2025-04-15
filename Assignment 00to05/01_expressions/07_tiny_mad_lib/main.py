from pathlib import Path

project_folder = Path("/mnt/data/Python_Projects/08_madlibs_generator")
project_folder.mkdir(parents=True, exist_ok=True)

# Create the main.py file
from colorama import init, Fore, Style
import time

# Initialize colorama
init(autoreset=True)

SENTENCE_START: str = f"{Fore.YELLOW}Panaversity is fun. I learned to program and used Python to make my "

def get_input(prompt: str) -> str:
    while True:
        user_input = input(prompt).strip()
        if user_input.isalpha():
            return user_input
        print(Fore.RED + "❌ Please enter only alphabetic characters.\n")

def main():
    print(Fore.CYAN + "="*50)
    print(Fore.GREEN + Style.BRIGHT + "🎉 Welcome to the Python Mad Libs Generator! 🎉")
    print(Fore.CYAN + "="*50 + "\\n")
    time.sleep(1)

    while True:
        adjective = get_input(Fore.MAGENTA + "👉 Please type an adjective and press enter: ")
        noun = get_input(Fore.MAGENTA + "👉 Please type a noun and press enter: ")
        verb = get_input(Fore.MAGENTA + "👉 Please type a verb and press enter: ")

        print()
        print(Fore.YELLOW + SENTENCE_START + Fore.BLUE + f"{adjective} {noun} {verb}!\\n")
        print(Fore.GREEN + "😄 Great sentence! Want to try again?\\n")

        again = input(Fore.CYAN + "🔁 Do you want to create another? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print(Fore.LIGHTRED_EX + "\\n👋 Thanks for playing Mad Libs! Bye bye!\n")
            break

if __name__ == '__main__':
    main()
