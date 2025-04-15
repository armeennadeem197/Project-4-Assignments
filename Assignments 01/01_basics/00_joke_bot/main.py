# Joke Bot Program

PROMPT: str = "What do you want? If you want a joke, type 'joke': "
JOKE: str = (
    "Here is a joke for you!\n"
    "Why do programmers prefer dark mode?\n"
    "Because the light attracts bugs!"
)
SORRY: str = "Sorry, I only tell jokes."

def main():
    user_input = input(PROMPT).strip().lower()  # Get user input, trim spaces, convert to lowercase

    if user_input == "joke":
        print("\n" + JOKE)
    else:
        print("\n" + SORRY)

if __name__ == "__main__":
    main()
