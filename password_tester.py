"""
This program takes a given user password and adds 'points' to that password,
then calculates the total amount of 'points'. The program will take the total
amount of points and then inform the user if they have a strong password or a
weak password.
"""

import re


def password_test():
    value = 0
    user_pass = input("Please enter a password for testing: ")
    if re.search('[a-z]', user_pass):
        value = value + 1
    if re.search('[A-Z]', user_pass):
        value = value + 1
    if re.search('[0-9]', user_pass):
        value = value + 1
    if re.search('[!@#$%^&*()~_+":?<>.,;-=]', user_pass):
        value = value + 1
    if len(user_pass) < 10:
        print("Your password should contain more than 10 characters\n")
    password_score(value)


def password_score(value):
    if value == 4:
        print("Strong Password")
    if value == 3:
        print("Medium Password")
    if value == 2:
        print("Weak Password")
    if value == 1:
        print("Very Weak Password, consider changing your password now.")
    return 0


if __name__ == '__main__':
    password_test()
