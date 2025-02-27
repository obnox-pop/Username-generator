import random

# Lists of adjectives and nouns
adjectives = [
    "Epic", "Funky", "Wild", "Savage", "Electric", "Mysterious", "Witty", "Grumpy",
    "Artisty", "Champion", "Legendary", "Quirky", "Shadow", "Frosty", "Cosmic", "Lunar"
]
nouns = [
    "Panda", "Warrior", "Storm", "Phoenix", "Ninja", "Explorer", "Wizard", "Pirate",
    "Gamer", "Samurai", "Slayer", "Vortex", "Squirrel", "Jaguar", "Dragon", "Ghost"
]
special_chars = ["_", ".", "-", ""]
numbers = list(range(10, 100))  # Two-digit numbers

def generate_username(add_number=True, add_special_char=True):
    """Generates a unique and fun username based on user preferences"""
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    char = random.choice(special_chars) if add_special_char else ""
    num = str(random.choice(numbers)) if add_number else ""

    return f"{adj}{char}{noun}{num}"

def main():
    """Main function to get user preferences, generate usernames, and save to file"""
    print("Customize your username generation:")
    
    # Get user preferences
    add_number = input("Include numbers? (yes/no): ").strip().lower() == "yes"
    add_special_char = input("Include special characters? (yes/no): ").strip().lower() == "yes"

    # Generate usernames
    usernames = [generate_username(add_number, add_special_char) for _ in range(10)]

    # Save to a file
    with open("usernames.txt", "w") as file:
        file.write("\n".join(usernames))

    # Display usernames
    print("\nHere are your unique username suggestions (saved to 'usernames.txt'):")
    for username in usernames:
        print(username)

if __name__ == "__main__":
    main()
