# Stone-Paper-Scissor Game

import random

# Available choices
choices = ["stone", "paper", "scissor"]

# Initialize scores
user_score = 0
computer_score = 0

print("Welcome to the Stone-Paper-Scissor Game!")
print("Type 'quit' anytime to exit the game.\n")

# Game loop
while True:
    user_choice = input("Enter your choice (stone, paper, scissor): ").lower()

    if user_choice == "quit":
        print("\nThanks for playing!")
        print(f"Final Score -> You: {user_score}, Computer: {computer_score}")
        break

    if user_choice not in choices:
        print("Invalid choice. Please try again.\n")
        continue

    # Computer makes a random choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Determine winner
    if user_choice == computer_choice:
        print("It's a tie!\n")
    elif (user_choice == "stone" and computer_choice == "scissor") or \
         (user_choice == "scissor" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "stone"):
        print("You win this round!\n")
        user_score += 1
    else:
        print("Computer wins this round!\n")
        computer_score += 1

    print(f"Current Score -> You: {user_score}, Computer: {computer_score}\n")
