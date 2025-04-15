def is_leap_year(year: int) -> bool:
    """
    Returns True if the given year is a leap year, otherwise False.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def main():
    try:
        # Get the year to check from the user
        year = int(input("Please input a year: "))

        # Check if it's a leap year
        if is_leap_year(year):
            print("That's a leap year!")
        else:
            print("That's not a leap year.")
    except ValueError:
        print("❌ Please enter a valid numeric year.")


if __name__ == '__main__':
    main()
