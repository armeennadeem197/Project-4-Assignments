🚀 Project-4-Assignments: Assignments 00 to 05
📂 02_lists/
1. add_many_numbers
Objective: Allow the user to add multiple numbers to a list.

Functionality: Takes user input and stores the numbers in a list.

Example: A program that prompts the user to input numbers and stores them in a list.

def add_many_numbers():
    numbers = []
    while True:
        num = input("Enter a number (or press Enter to stop): ")
        if num == "":
            break
        numbers.append(int(num))
    print("List of numbers:", numbers)

2. double_list
Objective: Double each element in a given list using a loop or list comprehension.

Functionality: Iterates through the list and doubles each element.

Example: [1, 2, 3] → [2, 4, 6].

def double_list(lst):
    doubled_lst = [x * 2 for x in lst]
    print("Doubled List:", doubled_lst)

3. erase_canvas
Objective: Clears all elements from a list, making it empty.

Functionality: This function removes all elements from a list.

Example: [1, 2, 3] → [].

def erase_canvas(lst):
    lst.clear()
    print("List after clearing:", lst)

4. get_first_element
Objective: Retrieve and display the first element of a list.

Functionality: Displays the first element in the list.

Example: [1, 2, 3] → 1.

def get_first_element(lst):
    if lst:
        print("First element:", lst[0])
    else:
        print("The list is empty.")

5. get_last_element
Objective: Fetch and print the last element of a list.

Functionality: Displays the last element in the list.

Example: [1, 2, 3] → 3.

def get_last_element(lst):
    if lst:
        print("Last element:", lst[-1])
    else:
        print("The list is empty.")

6. get_list
Objective: Displays the complete list so the user can see all stored elements.

Functionality: Prints out the entire list.

def get_list(lst):
    print("Complete List:", lst)


7. shorten
Objective: Reduces the size of a list by removing specific elements.

Functionality: Allows the user to remove elements based on certain conditions or by specifying which elements to remove.

Example: Remove specific values like 2 from the list [1, 2]

def shorten(lst, value_to_remove):
    while value_to_remove in lst:
        lst.remove(value_to_remove)
    print(f"List after removing {value_to_remove}:", lst)

📂 Folder Structure:
Project-4-Assignments/
│
└── Assignments 00 to 05/
    └── 02_lists/
        ├── add_many_numbers.py
        ├── double_list.py
        ├── erase_canvas.py
        ├── get_first_element.py
        ├── get_last_element.py
        ├── get_list.py
        └── shorten.py

🏗️ Usage:
Each Python file above can be executed independently, and you can modify them as per the assignment needs. For example, running the add_many_numbers.py will allow the user to enter numbers and store them in a list, and running the shorten.py script can allow the user to remove a specific value from a list.
