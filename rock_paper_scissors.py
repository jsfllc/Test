"""
A simple command line game that allows a user to play rock, paper, scissors with the
computer. This program will take the input of the user and then compare that to a randomly
selected item from the 'choices' list to determine if the player has won or lost. The
program will then display the choice of the user and computer and then display the outcome
of the game.
"""

import random

def play_game():
    print("Welcome to Rock, Paper, Scissors.")
    print("Choose either Rock, Paper, or Scissors and we will see who wins.")

    user_choice = input("GO: ").lower()
    choices = ['rock', 'paper', 'scissors']
    comp_choice = random.choice(choices)

    if user_choice == comp_choice:
        print("\nYour choice: " + user_choice)
        print("Computer's Choice: " + comp_choice)
        print("Its a tie.")

    elif (user_choice == 'paper' and comp_choice == 'scissors' or
            user_choice == 'rock' and comp_choice == 'paper' or
            user_choice == 'scissors' and comp_choice == 'rock'):
        print("\nYour choice: " + user_choice)
        print("Computer's Choice: " + comp_choice)
        print("You Lose")

    elif (user_choice == 'paper' and comp_choice == 'rock' or
            user_choice == 'rock' and comp_choice == 'scissors' or
            user_choice == 'scissors' and comp_choice == 'paper'):
        print("\nYour choice: " + user_choice)
        print("Computer's Choice: " + comp_choice)
        print("You Win!")


if __name__ == "__main__":
    play_game()
