# 📌 Get List - Python List Input Handling 🚀

This script allows the user to enter multiple values into a list and prints the final list. It is a great example of basic Python list operations, loops, and user input handling.

---

## 📌 Project Overview

- 📥 The program prompts the user to input values one by one.  
- ⏹ Pressing **Enter without typing anything** stops input collection.  
- 📋 Finally, the complete list is printed.

---

## 🛠️ How It Works

### 1️⃣ Initialize an Empty List (`lst`)
Creates an empty list to store user inputs.

### 2️⃣ User Input Loop
Continuously asks for user input.  
Pressing Enter stops the loop.

### 3️⃣ Print the Final List
Displays all user-entered values in a list format.

---

## 📜 Code Explanation

```python
def main():
    lst = []  # Initialize an empty list to store user inputs

    val = input("Enter a value: ")  # Get the first input from the user
    while val:  # Continue looping until the user presses Enter without typing anything
        lst.append(val)  # Add the input value to the list
        val = input("Enter a value: ")  # Ask for the next input

    print("Here's the list:", lst)  # Print the final list

if __name__ == '__main__':
    main()

🔹 main() - Program Execution
Initializes an empty list lst

Uses a while loop to keep accepting inputs

Stops when the user presses Enter without typing anything

Prints the final list after exiting the loop

🏗️ Project Structure
Project-4-Assignments/
└── Assignments 00 to 05/
    └── 02_lists/
        └── 07_get_list/
            └── main.py  # Main script to collect user input into a list

▶️ How to Run the Project
🔧 Prerequisites
Make sure Python is installed on your system.
Run python --version to check.

🏃 Run the Application
This will start the script and prompt the user to enter values one by one.

🎯 Expected Output
Enter a value: apple
Enter a value: banana
Enter a value: cherry
Enter a value: 
Here's the list: ['apple', 'banana', 'cherry']

🛠️ Customization Options
Modification | How to Implement
Convert inputs to numbers | Use int(input()) inside the loop
Limit number of inputs | Add a counter inside the loop
Display list length | Use print(len(lst)) after input ends

🧮 Example: Handling Numeric Input
def main():
    lst = []
    val = input("Enter a number (or press Enter to stop): ")
    while val:
        try:
            lst.append(int(val))  # Convert input to integer
        except ValueError:
            print("Please enter a valid number.")  # Handle non-numeric input
        val = input("Enter a number (or press Enter to stop): ")

    print("Here's the list:", lst)

if __name__ == '__main__':
    main()

🎯 Learning Outcomes
This project helps in understanding:

✅ User input handling in Python 🖥️
✅ Basic list operations 📋
✅ Loops and conditionals 🔄

💡 Final Thoughts
The Get List App is a beginner-friendly Python project that demonstrates list handling, user input loops, and printing lists.
Perfect for Python beginners exploring loops and user input! 🚀
