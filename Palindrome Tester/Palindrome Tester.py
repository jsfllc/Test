# Palindrome Tester
print("Author: John Farina \n")

# Title of the program as well as the purpose of the program
print("Palindrome Tester")
print("The purpose of this program is to test a string of text ")
print("and determine if that word is in fact, a palindrome.\n")


# Palindrome method, which disregards spaces in the user's input and reverses that string
# in order to test the input to see if it is a palindrome.
def palindrome():
    string = input("Please insert a palindrome: ")
    string = string.lower()
    if ' ' in string:
        string = string.replace(' ', '')
    if str(string) == str(string)[::-1]:
        return True
    return False


# Setting the value of "answer" equal to the palindrome method
answer = palindrome()

# If/else statement to determine which output is neccessary based on the outcome of
# the palindrome method.
if answer:
    print("The following string is a palindrome.\n")
else:
    print("The following string is not a palindrome.\n")
