import random

def roll_dice():
    # Generate random number between 1 and 6
    return random.randint(1, 6)

print("🎲 Welcome to Dice Rolling Simulator 🎲")

while True:
    # Ask user if they want to roll the dice
    choice = input("Do you want to roll the dice? (y/n): ").lower()

    if choice == "y":
        result = roll_dice()
        print(f" You rolled a {result} 🎯")
    elif choice == "n":
        print("Thanks for playing! Goodbye 👋")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
