import random
from enum import Enum, auto

class Choice(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()

def get_user_choice():
    """Get and validate user input"""
    while True:
        user_input = input("\nChoose rock, paper, or scissors (or 'q' to quit): ").lower()
        if user_input in ['q', 'quit']:
            return None
        if user_input in ['rock', 'r']:
            return Choice.ROCK
        if user_input in ['paper', 'p']:
            return Choice.PAPER
        if user_input in ['scissors', 's']:
            return Choice.SCISSORS
        print("Invalid choice! Please select rock, paper, or scissors.")

def determine_winner(user_choice, computer_choice):
    """Determine the game winner"""
    if user_choice == computer_choice:
        return "tie"
    if (user_choice == Choice.ROCK and computer_choice == Choice.SCISSORS) or \
       (user_choice == Choice.SCISSORS and computer_choice == Choice.PAPER) or \
       (user_choice == Choice.PAPER and computer_choice == Choice.ROCK):
        return "user"
    return "computer"

def play_game():
    """Main game function"""
    print("\n" + "="*30)
    print(" 🪨📄✂️ ROCK-PAPER-SCISSORS ✂️📄🪨 ")
    print("="*30)
    
    user_score = 0
    computer_score = 0
    
    while True:
        user_choice = get_user_choice()
        if user_choice is None:
            break
            
        computer_choice = random.choice(list(Choice))
        
        print(f"\nYou chose: {user_choice.name.title()}")
        print(f"Computer chose: {computer_choice.name.title()}")
        
        result = determine_winner(user_choice, computer_choice)
        
        if result == "tie":
            print("It's a tie! 🤝")
        elif result == "user":
            print("You win! 🎉")
            user_score += 1
        else:
            print("Computer wins! 😢")
            computer_score += 1
        
        print(f"\nScore - You: {user_score} | Computer: {computer_score}")
    
    print("\nThanks for playing! Final Scores:")
    print(f"You: {user_score} | Computer: {computer_score}")
    print("Goodbye! 👋")

if __name__ == "__main__":
    play_game()