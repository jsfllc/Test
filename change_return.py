"""
This program will ask a user to input the amount that is owed and then ask for
how much was given toward this total. The program will then output how much change
is due back.
"""

def change():
    print("How much is owed?")
    owed = input("$")
    print("How much was given?")
    given = input("$")

    total = float(given) - float(owed)
    print("The customer is due back $" + str(round(total, 2)))

if __name__ == '__main__':
    change()