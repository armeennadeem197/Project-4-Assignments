import random
from collections import defaultdict

# Enhanced Mad Libs Generator

def get_user_inputs():
    """Get user inputs with validation and variety"""
    inputs = {}
    
    print("🌟 Welcome to Advanced Mad Libs! 🌟\n")
    print("Please provide the following words:\n")
    
    inputs['name'] = input("Enter a name (e.g., Alice, Captain Sparklebeard): ")
    inputs['place'] = input("Enter a place (e.g., Wonderland, Mars, the fridge): ")
    inputs['animal'] = input("Enter an animal (e.g., quantum parrot, disco shark): ")
    inputs['verb'] = input("Enter a verb (e.g., dancing, teleporting, procrastinating): ")
    inputs['adjective'] = input("Enter an adjective (e.g., sparkly, existential, sus): ")
    inputs['food'] = input("Enter a food item (e.g., neutron star soup, rainbow tacos): ")
    inputs['emotion'] = input("Enter an emotion (e.g., bewildered, ecstatic, mildly concerned): ")
    
    return inputs

def select_story_template():
    """Let user choose or randomize story template"""
    templates = {
        1: "fantasy",
        2: "sci-fi",
        3: "horror",
        4: "romance",
        5: "random"
    }
    
    print("\nChoose a story genre:")
    for num, genre in templates.items():
        print(f"{num}. {genre.capitalize()}")
    
    while True:
        try:
            choice = int(input("\nEnter your choice (1-5): "))
            if 1 <= choice <= 5:
                if choice == 5:
                    return random.choice(list(templates.values())[:-1])
                return templates[choice]
            print("Please enter a number between 1-5")
        except ValueError:
            print("Invalid input. Please enter a number.")

def generate_story(inputs, genre):
    """Generate story based on genre and inputs"""
    stories = {
        "fantasy": [
            f"Legend tells of {inputs['name']}, who ventured to {inputs['place']} in search of the mythical {inputs['animal']}. ",
            f"To their {inputs['emotion']} surprise, the creature was {inputs['verb']} while wearing a {inputs['adjective']} crown. ",
            f"After offering it {inputs['food']}, they forged an alliance to save the kingdom from eternal boredom!"
        ],
        "sci-fi": [
            f"In the year 3142, astronaut {inputs['name']} crash-landed on {inputs['place']}. ",
            f"The first lifeform they encountered was a {inputs['adjective']} {inputs['animal']} {inputs['verb']} near the wreckage. ",
            f"Through the universal language of {inputs['food']}, they communicated and discovered a {inputs['emotion']} truth about the universe."
        ],
        "horror": [
            f"{inputs['name']} never should have gone to {inputs['place']}. ",
            f"The {inputs['adjective']} {inputs['animal']} was {inputs['verb']} in the shadows, filling them with {inputs['emotion']} dread. ",
            f"When it demanded {inputs['food']} as tribute, {inputs['name']} knew escape was impossible..."
        ],
        "romance": [
            f"It was in {inputs['place']} that {inputs['name']} first laid eyes on the most {inputs['adjective']} {inputs['animal']} they'd ever seen. ",
            f"The way it was {inputs['verb']} made their heart flutter with {inputs['emotion']} excitement. ",
            f"They bonded over shared {inputs['food']}, and the rest was history."
        ]
    }
    
    return "".join(stories[genre])

def add_special_effects(story):
    """Add some fun visual effects"""
    effects = [
        "\n✨ " + "*"*50 + " ✨",
        "\n💫 " + "~"*50 + " 🌈",
        "\n🚀 " + "="*50 + " 👽",
        "\n🧙 " + "_"*50 + " 🏰"
    ]
    return random.choice(effects) + "\n" + story + "\n" + random.choice(effects)

def main():
    """Run the advanced Mad Libs game"""
    while True:
        # Get all user inputs
        user_inputs = get_user_inputs()
        
        # Let user select story genre
        genre = select_story_template()
        
        # Generate the story
        story = generate_story(user_inputs, genre)
        
        # Add special effects
        final_story = add_special_effects(story)
        
        # Display the final story
        print("\nYour Amazing Mad Libs Story:\n")
        print(final_story)
        
        # Ask if user wants to play again
        play_again = input("\nWould you like to create another story? (yes/no): ").lower()
        if play_again not in ['y', 'yes']:
            print("\nThanks for playing Advanced Mad Libs! 🎉")
            break

if __name__ == "__main__":
    main()