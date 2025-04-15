🔢 Print Ones Digit Program
📌 Overview
This program extracts and prints the ones digit (last digit) of any integer, including negative numbers.

🛠 How It Works?
print_ones_digit(num: int)

The function extracts the ones digit using abs(num) % 10.

The abs() function ensures the program works for negative numbers as well.

It prints the ones digit of the number.

main()

Asks the user to enter a number.

Handles invalid inputs by prompting the user to enter a valid integer.

Calls print_ones_digit() to display the result.

🔍 Example Runs
Input 1:

Enter a number: 1234
Output:

The ones digit is 4
Input 2:

Enter a number: -567
Output:

The ones digit is 7
🔄 Edge Case Handling
If the user enters invalid input (e.g., "abc", "12.5"), the program will prompt:

Invalid input. Please enter a valid integer.
The program works correctly for negative numbers due to the use of abs(num).

