def subaract_seven(num: int) -> int:
    """
    Subaract 7 from the given number and return the result.
    """

    return num - 7

def main():
    num: int = 7
    num = subaract_seven(num)
    print("This should be zero:", num)


if __name__ == "__main__":
    main()