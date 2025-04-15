AFFIRMATION: str = "I am capable of doing anything I put my mind to."

def main():
    print("🔁 Affirmation Practice")
    print(f"\nPlease type the following affirmation exactly:\n➡️  {AFFIRMATION}\n")

    while True:
        user_feedback = input("Your input: ")
        if user_feedback == AFFIRMATION:
            print("\n✅ That's right! Keep believing in yourself! 💪")
            break
        else:
            print("❌ That wasn't quite right. Let's try again!\n")

if __name__ == '__main__':
    main()
