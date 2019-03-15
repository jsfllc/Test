"""
A simple program that will ask users for their username and then create a json
file to store that username in. If that name already exists within the json file,
it will print a welcome back message.
"""

import json


def username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What is your username? ")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you next time, " + username + "!")
    else:
        print("Welcome back, " + username + "!")


if __name__ == '__main__':
    username()