#Robert Drynan week 2
from random import random

choices = ["Rock", "Paper", "Scissors"]
playerChoice = random.randint(0,2)
computerChoice = random.randint(0,2)
if playerChoice == computerChoice:
    print("Draw")
elif playerChoice == 0 & computerChoice == 2:
    print("You win!")
elif playerChoice == 1 & computerChoice == 2:
    print("You lose!")
elif playerChoice == 2 & computerChoice == 1:
    print("You win!")
elif playerChoice ==