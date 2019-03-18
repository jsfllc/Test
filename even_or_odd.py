"""
This program tests if a number given by the user is either even or odd by using
the equation of (user input) modulo 2. If the outcome of this equation is zero,
then the program will tell the user their number is even, if the outcome is not
zero, then the program will tell the user their number is odd.
"""


def even_odd():
    e_or_o = int(input("Please enter a number to test if it is even or odd: "))

    if e_or_o % 2 == 0:
        print("The number " + str(e_or_o) + " is even.")

    else:
        print("The number " + str(e_or_o) + " is odd.")


if __name__ == "__main__":
    even_odd()