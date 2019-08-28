"""
This program recites the song lyrics of '99 Bottles of Beer'.
In it, the program goes through a loop that will subtract one from
the starting bottles number of 99 until it reaches zero.
"""


def count_bottles():
    bottles = 99
    while True:
        if bottles >= 2:
            print(str(bottles) + " bottles of beer on the wall, " 
            + str(bottles) + " bottles of beer.")
            bottles -= 1
            print("You take one down and pass it around, " 
            + str(bottles) + " bottles of beer of the wall.\n")
        elif bottles == 1:
            print(str(bottles) + " bottle of beer on the wall " 
            + str(bottles) + " bottle of beer.")
            bottles = 0
            print("You take one down and pass it around, " 
            + str(bottles) + " bottles of beer of the wall.")
        else:
            break


if __name__ == '__main__':
    count_bottles()
