"""
This program takes a list of numbers provided by a user and will either find the
mean, median, or mode depending on the choice of the user.
"""

import statistics as stat


def calculator():
    numbers = [int(number) for number in
    input("Please enter a list of numbers (sepeate your list with spaces): ").split()]
    choice = input("\nWould you like to find the mean, median, or mode of these numbers?: ").lower()

    if choice == "mean":
        mean = stat.mean(numbers)
        print("\nThe mean of your numbers is: " + str(round(float(mean), 2)))

    elif choice == "median":
        median = stat.median(numbers)
        print("\nThe median of your numbers is: " + str(median))

    elif choice == "mode":
        mode = stat.mode(numbers)
        print("\nThe mode of your numbers is: " + str(mode))


if __name__ == '__main__':
    calculator()
