# 📌 Project 04: Age Riddle Solver
# 👩‍💻 Author: Amna Khalil
# 🗓️ Date: April 2025
# 🔍 Description: Solves a riddle about the ages of five friends using variable assignments.

from termcolor import colored
import time

def main():
    # 🎉 Welcome Message
    print(colored("\n\t🧠 Welcome to the Age Riddle Solver! 🧮", "light_magenta", attrs=["bold"]))
    print(colored("Let's solve the ages of Anton, Beth, Chen, Drew, and Ethan.\n", "cyan"))
    time.sleep(1)
    
    anton = 21
    beth = anton + 6
    chen = beth + 20
    drew = chen + anton
    ethan = chen

    # ✅ Output
    print(colored(f"Anton is {anton}", "green"))
    print(colored(f"Beth is {beth}", "green"))
    print(colored(f"Chen is {chen}", "green"))
    print(colored(f"Drew is {drew}", "green"))
    print(colored(f"Ethan is {ethan}", "green"))

    print(colored("\nThanks for solving the riddle with Us! 🎉", "light_yellow", attrs=["bold"]))

if __name__ == '__main__':
    main()
