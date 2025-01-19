# Import the random library to use for the dice later
import random
#array of weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]
#rolls the dice to choose the weapon
try:
    weaponRoll = random.randint(1, 6)
    hero_combat_strength = weaponRoll
    weapon = weapons[weaponRoll - 1]
    print(f"The Hero's weapon is a: {weapon}")
    if weaponRoll <= 2:
        print("You rolled a weak weapon, friend")
    elif weaponRoll <= 4:
        print("Your weapon is meh")
    else:
        print("Nice weapon, friend!")


    if weapon != "Fist":
        print("Thank goodness you didn't roll the Fist...")

except ValueError:
    print("Invalid input enter an integer, please try again.")