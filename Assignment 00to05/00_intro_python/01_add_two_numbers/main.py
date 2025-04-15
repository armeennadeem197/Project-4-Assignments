# Program: Add Two Numbers
# Created By: Amna Khalil
# Institute: GIAIC
# Description:

# This program allows the user to input two numbers,
# calculates their sum, and displays the result.

# It also gives the user the option to run the program again.


# ANSI escape codes for text colors
RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def main():
    print(f"{CYAN}🔷 Welcome to the Add Two Numbers Program! 🔷{RESET}")
    print(f"{YELLOW}👩‍💻 Created by: Amna Khalil{RESET}\n")

    while True:
        # Get two valid integers from user
        num1 = get_number("🟡 Enter the first number: ")
        num2 = get_number("🟡 Enter the second number: ")

        # Calculate and show result
        total = num1 + num2
        print(f"\n{GREEN}✅ The total of {num1} and {num2} is: {YELLOW}{total}{RESET}\n")

        # Ask user if they want to run again
        run_again = input(f"{CYAN}🔁 Do you want to run the program again? (yes/no): {RESET}").strip().lower()
        if run_again not in ['yes', 'y']:
            print(f"\n{GREEN}✨ Thank you for using the program. Goodbye! ✨{RESET}")
            break
        print()  # line break before next round

def get_number(prompt):
    
   # Keep asking until user provides a valid integer.
    
    while True:
        value = input(prompt)
        try:
            return int(value)
        except ValueError:
            print(f"{RED}❌ Please enter a valid number.{RESET}")

# Run the main function if this file is executed
if __name__ == '__main__':
    main()
