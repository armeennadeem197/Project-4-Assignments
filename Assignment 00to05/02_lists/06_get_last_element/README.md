📌 Get Last Element - Python Script 🐍
This project contains a simple Python program that retrieves and prints the last element from a user-generated list. It's a great example of how to handle user input, lists, and basic function structuring in Python.

📌 Project Overview
🧑‍💻 The user enters elements one by one.

⌨️ Pressing Enter without input stops the process.

✅ The program then prints the last element of the list.

🛠️ How It Works
1️⃣ get_lst() – Gather List Input
Prompts the user to enter values until they press Enter.

def get_lst():
    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop: ")
    return lst
2️⃣ get_last_element(lst) – Print the Last Element
Displays the last item in the list.

def get_last_element(lst):
    print(lst[-1])
📝 Tip: This will raise an error if the list is empty. You can handle that like this:

def get_last_element(lst):
    if lst:
        print("Last element:", lst[-1])
    else:
        print("The list is empty!")
3️⃣ main() – Execute the Program
def main():
    lst = get_lst()
    get_last_element(lst)

if __name__ == '__main__':
    main()
▶️ How to Run
💡 Prerequisites:
Python installed (python --version)

🏃 Run the script:
python main.py
🎯 Example Output
Please enter an element of the list or press enter to stop: dog
Please enter an element of the list or press enter to stop: cat
Please enter an element of the list or press enter to stop: rabbit
Please enter an element of the list or press enter to stop: 
rabbit
🔧 Customization Ideas

Feature	How to Add
Handle empty list	Add a check before accessing lst[-1]
Allow numeric inputs	Use int(input()) or float(input()) in get_lst()
Let user pick index	Ask for an index and print lst[index] safely
🧠 Learning Goals
✅ Input collection via loops

✅ Accessing list elements (negative index)

✅ Creating reusable functions

✅ Error handling and input validation

🌱 Future Enhancements
Add support for numeric or mixed input types

Validate index range if selecting by index

Save user input to a file

📌 Summary
This is a clean and practical script that demonstrates how to get the last item from a list entered by the user. It's simple, useful, and a great foundation for learning Python. 🎉

