import random

def play_game():
    while True:
        # User Input
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        while user_choice not in ["rock", "paper", "scissors"]:
            user_choice = input("Invalid choice. Enter rock, paper, or scissors: ").lower()

        # Computer Selection
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        # Display choices
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}\n")

        # Game Logic
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            result = "You win!"
        else:
            result = "You lose!"

        # Display result
        print(result)

        # Play Again
        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            break

# Run the game
play_game()