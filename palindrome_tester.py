"""
The purpose of this program is to test a string of text
and determine if that word is a palindrome.
"""

# Palindrome method, which disregards spaces in the user's input and reverses that string
# in order to test the input to see if it is a palindrome.
def palindrome():
    string = input("Please insert a palindrome: ").lower()
    if ' ' in string:
        string = string.replace(' ', '')
    elif str(string) == str(string)[::-1]:
        print("The following string is a palindrome.\n")
    else:
        print("The following string is not a palindrome.\n")
        

if __name__ == '__main__':
    palindrome()
