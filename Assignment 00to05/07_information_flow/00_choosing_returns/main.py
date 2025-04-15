ADULT_AGE: int = 18  # U.S. adult age threshold

def is_adult(age: int):
    """Returns True if the age is 18 or older, otherwise False."""
    if age >= ADULT_AGE:
        return True
    return False
def main():
    # Get the age input and convert it to an integer
    age: int = int(input("How old is the person?: "))
    print(is_adult(age))  # Print whether the person is an adult

# Check if the script is run directly
if __name__ == "__main__":
    main()
