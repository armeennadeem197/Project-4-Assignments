import os

# Conversion factor from feet to inches
INCHES_IN_FOOT: int = 12

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        clear_screen()
        print("\033[1;32m==========================================")
        print("        🌟 Welcome to the Feet to Inches Converter 🌟")
        print("==========================================\033[0m")
        print("\033[1;34mConvert feet to inches easily!\033[0m")
        
        try:
            feet: float = float(input("\033[1;35mEnter number of feet: \033[0m"))  # Take input from user
            if feet <= 0:
                print("\n\033[1;31m❌ Please enter a positive number for feet.\033[0m")
                input("\033[1;34mPress Enter to try again...\033[0m")
                continue
        except ValueError:
            print("\n\033[1;31m❌ Invalid input. Please enter a valid number.\033[0m")
            input("\033[1;34mPress Enter to try again...\033[0m")
            continue

        inches: float = feet * INCHES_IN_FOOT  # Conversion formula

        print("\n---------------- Calculation ----------------")
        print(f"\033[1;36mThat is {inches} inches!\033[0m")
        print("----------------------------------------------\n")

        again = input("\033[1;34mWould you like to convert another feet value? (yes/no): \033[0m").strip().lower()
        if again not in ('yes', 'y'):
            print("\n\033[1;32mThank you for using the Feet to Inches Converter! 🌟\n\033[0m")
            break

if __name__ == '__main__':
    main()
