"""
The purpose of this program is to simulate rolling a pair of dice. When the user
is ready, he/she will enter 'roll' and the program will enter a random pair of
numbers between 1 and 6. If the user enters anything other than roll into the program
then the program will ask the user for the correct input and restart itself.
"""

import random

def roll():
    dice1 = random.randint(1, 7)
    dice2 = random.randint(1, 7)

    while True:
        roll = input("When you're ready, type 'roll' to roll the dice: ").lower()

        if roll == "roll":
            print("\nThe first die was " + str(dice1))
            print("The second die was " + str(dice2))
            break

        else:
            print("Please enter 'roll' when you are ready to roll the dice.\n")


if __name__ == "__main__":
    roll()
