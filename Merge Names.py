# Merge Names
print("Author: John Farina \n")

# Program name and purpose of the program
print("Merge Names")
print("The purpose of this program is to combine a list of first names ")
print("with a list of last names, and, in turn, form a first and last name list\n")

# Input that asks users for a list of first names separated by a comma
# and then sets those inputs into values in the firstList list
firstName = input("Please provide list of first names separated by comma, e.g. John,Kim,Kate: ")
firstList = list(map(str, firstName.split(',')))

# Input that asks users for a list of last names separated by a comma
# and then sets those inputs into values in the lastList list
lastName = input("Please provide list of last names separated by comma, e.g. Davidson,Hunter,Johnson: ")
lastList = list(map(str, lastName.split(',')))

# Initializing the firstLastList list, which combines both the firstList and lastList, above
firstLastList = list(zip(firstList, lastList))
print()

# Output of the firstList and lastList lists and then zips the entities together into
# (firstname and lastname) pairs
print("The list of first names is: " + str(firstList))
print("The list of last names is: " + str(lastList))
print("The list of first and last names is: " + str(firstLastList).replace(',', ''))
