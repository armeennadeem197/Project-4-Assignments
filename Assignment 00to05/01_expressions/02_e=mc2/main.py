# Mass-Energy Converter

import os

# Speed of light in m/s
C: int = 299792458

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculate_energy(mass: float) -> float:
    """
    Calculate the energy using Einstein's formula E = m * c^2
    """
    return mass * (C ** 2)

def main():
    while True:
        clear_screen()
        print("""
==========================================
        🌟 Welcome to the Mass-Energy Converter 🌟
==========================================
Einstein's famous equation: E = m * C^2
Let's calculate how much energy is in your mass!
        """)

        try:
            mass_in_kg: float = float(input("Enter mass in kilograms (kg): "))
            if mass_in_kg <= 0:
                print("\n❌ Please enter a positive number for mass.")
                input("Press Enter to try again...")
                continue
        except ValueError:
            print("\n❌ Invalid input. Please enter a valid number.")
            input("Press Enter to try again...")
            continue

        energy_in_joules: float = calculate_energy(mass_in_kg)

        print("\n---------------- Calculation ----------------")
        print("e = m * C^2")
        print(f"m = {mass_in_kg} kg")
        print(f"C = {C} m/s")
        print(f"\n⚡ {energy_in_joules:.3e} joules of energy!")
        print("----------------------------------------------\n")

        again = input("Would you like to convert another mass? (yes/no): ").strip().lower()
        if again not in ('yes', 'y'):
            print("\nThank you for using the Mass-Energy Converter! 🚀\n")
            break

if __name__ == '__main__':
    main()
