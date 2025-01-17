#Robert Drynan week 2
import random

choices = ["Rock", "Paper", "Scissors"]

def main():
    try:
        choice = random.choice(choices)
        user_input = input("Please enter your choice (Rock, Paper, Scissors): ").capitalize()
        if user_input not in choices:
            raise ValueError("Please enter a valid choice - Rock, Paper, Scissors")
        player_choice = choices.index(user_input)
        #random computer choice
        computer_choice = random.randint(0,2)
        print(f"player choice: {choices[player_choice]}")
        print(f"computer choice: {choices[computer_choice]}")
        #who wins
        if computer_choice == player_choice:
            print("Draw")
        elif ((player_choice == 0 & computer_choice == 2) or
              (player_choice == 1 & computer_choice == 0) or
              (player_choice == 2 & computer_choice == 1)):
            print("You win")
        else:
            print("You lose")
    except ValueError as e:
        print(f"Error: {e}")