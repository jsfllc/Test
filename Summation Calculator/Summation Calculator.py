"""
Author: John Farina
Purpose: The purpose of this program is to calculate the sum of the numbers
        between a set of two numbers.
"""


# Summation

print("Author: John Farina \n")

# Title of program, including parameters that should be followed in order for the program to run correctly
print("Summation Calculator")
print("**Inputs must be positive integers, characters and/or negative integers will not be accepted**")
print("**The first integer must be less than or equal to the second integer**\n")

# While statement that tests to see if user input follows the set parameters
# If the user input is incorrect, the program will notify the user to try their input again.
while True:
    firstNum = input("Please enter the first integer value: ")
    secondNum = input("Please enter the second integer value: ")
    if (
            firstNum.isdigit() and
            secondNum.isdigit() and
            int(firstNum) >= 0 and
            int(secondNum) >= 0 and
            int(firstNum) <= int(secondNum)):
                break
    else:
        print("\nInvalid input, please try again.\n")


# Result method, which adds the integers between the two user inputs
def result():
    res = 0
    for i in range(int(firstNum), int(secondNum) + 1):
        res += i
    return res


# Print statement that returns the user's inputs as well as the summation of those inputs
print("The result of the summation between the integers {} and {} is: {}\n"
      .format(firstNum, secondNum, result()))
