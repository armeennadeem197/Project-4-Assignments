def main():
    try:
        curr_value = int(input("Enter a number: "))
        
        print("\n🔁 Doubling until we reach 100 or more:\n")
        while curr_value < 100:
            curr_value *= 2
            print(curr_value)
    except ValueError:
        print("❌ Please enter a valid number.")

if __name__ == '__main__':
    main()
