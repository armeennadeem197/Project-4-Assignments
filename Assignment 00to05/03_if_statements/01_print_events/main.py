def print_even_numbers(count=20):
    """
    Prints the first `count` even numbers starting from 0.
    """
    for i in range(count):
        even_number = i * 2
        print(even_number)

if __name__ == "__main__":
    print_even_numbers()
