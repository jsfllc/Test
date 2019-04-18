"""
This program is a mpg calculator. The program will ask a user
how many miles were driven on a tank of gas. Then the program will
ask the user how many gallons were added to the user's tank. Finally,
the program will calculate the mpg for the user's vehicle and display
this amount.
"""


def mpg_calc():
    miles = float(input("How many miles were driven on the tank of gas? "))
    gallons = float(input("How many gallons were fueled into the vehicle? "))
    mpg = float(miles / gallons)

    print("\nAfter driving " + str(miles) + " miles and adding " + str(gallons) +
          " gallons of fuel to your vehicle, your vehicle uses " + str(round(mpg, 2)) +
          " miles per gallon.")


if __name__ == '__main__':
    mpg_calc()
