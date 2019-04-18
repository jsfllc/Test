"""
This program asks a user for a string and then takes that word or phrase and outputs
its respected MD5 hash value.
"""

import hashlib

def md5_converter():
    phrase = input("What is the word or phrase you would like the MD5 hash of?: ")
    hashed = hashlib.md5(phrase.encode())

    print("\nThe md5 hash of your phrase is: ", end ="")
    print(hashed.hexdigest())

if __name__ == '__main__':
    md5_converter()
