# 🔥 Project 03: Fahrenheit to Celsius Converter
# Author: Amna Khalil
# Description: This program converts Fahrenheit temperature to Celsius.
# It includes input validation, colored output, and an option to repeat the conversion.

from termcolor import colored

def convert_temperature():
    print(colored("\n" + "="*60, "light_magenta"))
    print(colored("🌟 Welcome to the Fahrenheit ➡️ Celsius Converter! 🌟", "cyan", attrs=["bold"]))
    print(colored("Convert temperatures with ease and stay weather-smart ☀️❄️", "light_green"))
    print(colored("="*60 + "\n", "light_magenta"))

    while True:
        try:
            f = float(input(colored("📥 Enter temperature in Fahrenheit: ", "light_cyan")))
            c = (f - 32) * 5.0 / 9.0
            print(colored(f"\n✅ Temperature: {f}°F = {c:.2f}°C", "yellow"))
        except ValueError:
            print(colored("❌ Invalid input! Please enter a valid number.\n", "red"))
            continue

        again = input(colored("\n🔁 Do you want to convert another temperature? (yes/no): ", "light_blue")).strip().lower()
        if again not in ["yes", "y"]:
            print(colored("\n💚 Thanks for using the converter! Stay cool or warm 😄\n", "green", attrs=["bold"]))
            break

# Standard boilerplate to run the function
if __name__ == '__main__':
    convert_temperature()
