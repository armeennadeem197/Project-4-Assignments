def get_first_element(lst):
    if lst:  # Check if list is not empty
        print("First element:", lst[0])
    else:
        print("The list is empty. No first element.")

def get_lst():
    lst = []
    elem = input("Please enter an element of the list or press Enter to stop: ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press Enter to stop: ")
    return lst

def main():
    lst = get_lst()  # Get user-inputted list
    get_first_element(lst)  # Print first element if exists

if __name__ == '__main__':
    main()
