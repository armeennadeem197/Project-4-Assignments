def main():
    curr_value = int(input("Enter a starting number (less than 100): "))

    print("\nDoubling until we reach at least 100...\n")

    while curr_value < 100:
        curr_value *= 2
        print(f"Current value: {curr_value}")

if __name__ == '__main__':
    main()
