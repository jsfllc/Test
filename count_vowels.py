"""
A simple script to count the number of vowels in a sentence given as input.
"""


def count_vowels():
    vowels = 0
    count_vowel = input("Please enter a word or phrase: ").lower()
    vowel_dic = ['a', 'e', 'i', 'o', 'u']
    for vowel in count_vowel:
        if vowel in vowel_dic:
            vowels += 1

    print("Your phrase has " + str(vowels) + " vowels.")


if __name__ == '__main__':
    count_vowels()
