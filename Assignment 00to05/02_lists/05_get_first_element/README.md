# 📌 Get First Element - Python Script 🚀

This repository contains a beginner-friendly Python program that retrieves and prints the **first element** from a user-generated list. It’s a simple yet powerful example to learn about **user input**, **list handling**, and **modular programming** in Python. 🐍

---

## 📌 Project Overview

✅ Users can enter list items one at a time  
✅ Entry stops when the user presses Enter on an empty input  
✅ The program then prints the first element of the list (if any)

---

## 🛠️ How It Works

### 1️⃣ `get_lst()` – User Input Function

Prompts the user to enter elements until an empty input is given:

```python
def get_lst():
    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop: ")
    return lst

2️⃣ get_first_element(lst) – Retrieve First Element
Prints the first element if the list is not empty:

def get_first_element(lst):
    if lst:
        print("First element:", lst[0])
    else:
        print("The list is empty!")

3️⃣ main() – Program Entry Point
Handles full program flow:

python
Copy
Edit
def main():
    lst = get_lst()
    get_first_element(lst)

if __name__ == '__main__':
    main()
📂 Project Structure
css
Copy
Edit
Project-4-Assignments/
└── Assignments 00 to 05/
    └── 02_lists/
        └── 05_get_first_element/
            └── main.py  # Main script
▶️ How to Run
🔧 Prerequisites
Ensure Python is installed:

bash
Copy
Edit
python --version
🏃 Run the Script
bash
Copy
Edit
python main.py
🎯 Sample Output
text
Copy
Edit
Please enter an element of the list or press enter to stop: apple
Please enter an element of the list or press enter to stop: banana
Please enter an element of the list or press enter to stop: 
First element: apple
🛠️ Customization Options

Modification	How to Implement
Handle empty lists	Add a check inside get_first_element()
Convert input to integers	Use int(input(...)) in get_lst()
Retrieve any index	Use lst[index] after checking index bounds
Example: Safe Retrieval
python
Copy
Edit
def get_first_element(lst):
    if lst:
        print(lst[0])
    else:
        print("The list is empty!")
🎯 Learning Outcomes
✅ Accepting user input
✅ Working with lists
✅ Function-based program design
✅ Simple error handling

🔮 Future Enhancements
🛡️ Validate input types (e.g., numbers only)
🔁 Allow user to retrieve element by index
📦 Save the list to a file for reuse
