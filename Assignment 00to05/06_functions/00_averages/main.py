def average(a: float, b: float) -> float:
    """
    Returns the number which is halfway between a and b.
    """
    return (a + b) / 2  # Return the average of two numbers

def main():
    avg_1 = average(0, 10)       # First average: 5.0
    avg_2 = average(8, 10)       # Second average: 9.0

    final = average(avg_1, avg_2)  # Final average: (5.0 + 9.0) / 2 = 7.0

    print("avg_1:", avg_1)
    print("avg_2:", avg_2)
    print("final:", final)

if __name__ == '__main__':
    main()
