# 📌 Shorten List - Python List Trimming Program 🚀

This script limits a list to a maximum length of 3 by removing excess elements from the end. It demonstrates list manipulation, loops, and user input handling in Python.

---

### 🛠️ Features:
- Interactive user input for list elements
- Automatic trimming of lists exceeding 3 elements
- Visual feedback showing removed elements
- Clean and simple Python implementation

---

### 🎯 Example Usage:
```bash
Please enter an element of the list or press enter to stop: apple
Please enter an element of the list or press enter to stop: banana
Please enter an element of the list or press enter to stop: cherry
Please enter an element of the list or press enter to stop: mango
Please enter an element of the list or press enter to stop: 
mango
Final List: ['apple', 'banana', 'cherry']

🔧 Customization Options:
Change max length: Modify MAX_LENGTH in the code to change the maximum number of items allowed in the list.

Print final list: Add print(lst) after the shorten(lst) function call to display the final list after trimming.

Remove from the start: If you want to remove elements from the beginning of the list, use lst.pop(0) instead of lst.pop().

📚 Learning Outcomes:
List manipulation: Learn how to add and remove elements from a list dynamically.

Loops & input handling: Get familiar with using loops to handle continuous user input and conditional logic.

List size constraints: Implement a mechanism to enforce constraints on the size of a list.


📝 Code Explanation:
MAX_LENGTH = 3  # Define maximum allowed list length

def shorten(lst):
    """Trim list to MAX_LENGTH by removing elements from the end"""
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()  # Remove last element
        print(last_elem)  # Print removed element

def get_lst():
    """Collect user input to build list"""
    lst = []
    while True:
        elem = input("Please enter an element of the list or press enter to stop: ")
        if elem == "":
            break
        lst.append(elem)
    return lst

def main():
    """Main program flow"""
    lst = get_lst()  # Collect list items from the user
    shorten(lst)  # Shorten the list if necessary
    print("\nFinal List:", lst)  # Print the final list after trimming

if __name__ == '__main__':
    main()  # Run the main function

How to Run:
Ensure Python is installed (python --version).

Run the script with:
python main.py

Customization:
Change max list length: Modify MAX_LENGTH = <new_value> to set the desired maximum number of items in the list.

Print final list: After the call to shorten(lst), add print(lst) to display the final list.
