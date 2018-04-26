"""
Author: John Farina

This is a program/game that implements a Binary Search by
making the computer play Hi-Lo. In this program, the computer
will guess a user's number that is in between 1 and a higher
number that is decided by the user in seven guesses.
"""

print("I am willing to bet I can guess any number in the range of your "
      "choosing.\n")

guessList = 0   # Variable that keeps count of number of guesses
lowNumber = 1   # Variable that represents the beginning of the range

# While statement to make sure user is inserting a positive integer
while True:
    try:
        highNumber = int(input("The top number of your range, starting at one, is: "))  # User input to determine the end of the range
    except ValueError:
        print("Invalid response, please enter an integer.")
        continue
    if highNumber < 0:
        print("Please insert a positive integer.")
    else:
        break

# While statement that takes user input and determines the best course of action
guessing = True
while guessing:
    guess = (lowNumber + highNumber) // 2   # Equation that makes it possible for computer to guess the user's number
    print("Your number has to be {}, right?".format(guess))
    hiLowInput = input("Let me know if the guess is too high with >, "
                       "to low with <, "
                       "or y if I guessed your number. ".lower())
    guessList += 1  # Adds 1 to the guess count every time the computer guesses the user's number

    # if, elif, and else statements that determines what output is appropriate depending on the user's input
    if hiLowInput == ">":
        highNumber = guess
        guess = (lowNumber + guess) // 2
    elif hiLowInput == "<":
        lowNumber = guess
        guess = (highNumber + lowNumber) // 2
    elif hiLowInput == "y":
        guessing = False
        print("\nI guessed your number in {} tries! Your number was {}.".format(guessList, guess))
    else:
        print("\nIncorrect input, please enter >, <, or y.\n")
print("Thanks for playing!")
