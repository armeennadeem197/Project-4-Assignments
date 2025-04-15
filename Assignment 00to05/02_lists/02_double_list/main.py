# Function to double each number in a list
def double_numbers(numbers: list[int]) -> list[int]:
    return [num * 2 for num in numbers]  # List comprehension for efficiency

# Main function to demonstrate the functionality
def main():
    numbers = [1, 2, 3, 4]  # Original list
    doubled_numbers = double_numbers(numbers)  # Get the doubled list
    print(doubled_numbers)  # Print the result

# Entry point of the script
if __name__ == '__main__':
    main()
