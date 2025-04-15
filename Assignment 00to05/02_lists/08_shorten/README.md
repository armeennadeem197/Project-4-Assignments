"""
📌 Shorten List - Python List Trimming Program 🚀

This script limits a list to a maximum length of 3 by removing excess elements from the end.
It demonstrates list manipulation, loops, and user input handling in Python.

🛠️ Features:
- Interactive user input for list elements
- Automatic trimming of lists exceeding 3 elements
- Visual feedback showing removed elements
- Clean and simple Python implementation

🎯 Example Usage:
Please enter an element of the list or press enter to stop: apple
Please enter an element of the list or press enter to stop: banana
Please enter an element of the list or press enter to stop: cherry
Please enter an element of the list or press enter to stop: mango
Please enter an element of the list or press enter to stop: 
mango
Final List: ['apple', 'banana', 'cherry']

🔧 Customization Options:
1. Change max length: Modify MAX_LENGTH
2. Print final list: Add print(lst) after shorten()
3. Remove from start: Use pop(0) instead of pop()

📚 Learning Outcomes:
- List manipulation (adding/removing elements)
- Loops & input handling
- List size constraints
"""

MAX_LENGTH = 3  # Define maximum allowed list length

def shorten(lst):
    """Trim list to MAX_LENGTH by removing elements from end"""
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
    lst = get_lst()
    shorten(lst)
    print("\nFinal List:", lst)

if __name__ == '__main__':
    main()


🔧 Customization Options
Modification	How to Implement
Change max list length	Modify MAX_LENGTH = <new_value>
Print final list	Add print(lst) after shorten(lst)
Remove from beginning	Use lst.pop(0) instead of lst.pop()


📚 Learning Outcomes
List manipulation (adding & removing elements) 📋

Using loops & conditions for input handling 🔄

Understanding list size constraints 🛠️

Basic Python programming concepts 🐍
