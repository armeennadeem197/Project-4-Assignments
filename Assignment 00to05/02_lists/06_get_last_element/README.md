# 📌 Get Last Element - Python Script 🐍

This project contains a beginner-friendly Python script that retrieves and prints the **last element** from a user-generated list. It’s a simple yet effective example for understanding **user input**, **list operations**, and **function structuring** in Python.

---

## 📌 Project Overview

🧑‍💻 Users enter elements one by one  
⌨️ Input ends when the user presses Enter on an empty line  
✅ The program then prints the **last element** of the list

---

## 🛠️ How It Works

### 1️⃣ `get_lst()` – Gather List Input

Prompts the user to enter values until they stop by pressing Enter:

```python
def get_lst():
    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop: ")
    return lst

2️⃣ get_last_element(lst) – Print the Last Element
Prints the last element of the list. Handles empty lists safely:
def get_last_element(lst):
    if lst:
        print("Last element:", lst[-1])
    else:
        print("The list is empty!")

3️⃣ main() – Execute the Program
Runs the full logic from input to output:

def main():
    lst = get_lst()
    get_last_element(lst)

if __name__ == '__main__':
    main()

▶️ How to Run
💡 Prerequisites
Ensure Python is installed:
python --version

🏃 Run the Script
python main.py

🎯 Example Output
Please enter an element of the list or press enter to stop: dog
Please enter an element of the list or press enter to stop: cat
Please enter an element of the list or press enter to stop: rabbit
Please enter an element of the list or press enter to stop: 
Last element: rabbit

🔧 Customization Ideas
Feature | How to Add
Handle empty list | Add a check before accessing lst[-1]
Allow numeric inputs | Use int(input(...)) or float(input(...))
Let user pick index | Ask for an index and safely access lst[index]

🧠 Learning Goals
✅ Collect input in loops
✅ Access list elements using negative indexing
✅ Write modular and reusable functions
✅ Handle errors and edge cases effectivel

🌱 Future Enhancements
Support numeric or mixed input types

Validate index ranges if allowing user-defined index

Save the input list to a file for reuse
