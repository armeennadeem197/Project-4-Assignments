def get_last_element(lst):
    if lst:  # Check if the list is not empty
        print(lst[-1])  # Print last element
    else:
        print("The list is empty!")  # Handle empty list case


def get_lst():
    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":  # Keep adding elements until the user presses Enter
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop: ")
    return lst


def main():
    lst = get_lst()  # Get user-inputted list
    get_last_element(lst)  # Print last element


if __name__ == '__main__':
    main()
