"""
This is a program/game that implements a Binary Search by
making the computer play Hi-Lo. In this program, the computer
will guess a user's number that is in between 1 and a higher
number that is decided by the user in seven guesses.
"""

import sys


class HighLow:
    def __init__(self):
        self.test()

    def test(self):
        print("I am willing to bet I can guess any number in the range of your "
              "choosing.\n")
        # While statement to make sure user is inserting a positive integer
        while True:
            try:
                high_number = int(input("The top number of your range, starting at one, is: "))  # User input to
                # determine the end of the range
            except ValueError:
                print("Invalid response, please enter an integer.\n")
                continue

            if high_number < 0:
                print("Please insert a positive integer.\n")

            else:
                self.high_low_guess(high_number)

    def high_low_guess(self, high_number):
        guess_list = 0   # Variable that keeps count of number of guesses
        low_number = 1   # Variable that represents the beginning of the range

        # While statement that takes user input and determines the best course of action
        while True:
            # Equation that makes it possible for computer to guess the user's number
            guess = (low_number + high_number) // 2
            print("\nYour number has to be {}, right?".format(guess))
            hi_low_input = input("Let me know if the guess is too high with >, to low with <, "
                                 "or y if I guessed your number. ".lower())

            # if, elif, and else statements that determines what output is appropriate depending on the user's input
            if hi_low_input == ">":
                high_number = guess
                (low_number + guess) // 2
                guess_list += 1

            elif hi_low_input == "<":
                low_number = guess
                (high_number + low_number) // 2
                guess_list += 1

            elif hi_low_input == "y":
                print("\nI guessed your number in {} tries! Your number was {}.".format(guess_list, guess))
                print("Thanks for playing!")
                sys.exit()

            else:
                print("\nIncorrect input, please enter >, <, or y.")


if __name__ == '__main__':
    HighLow()
