# Write a function called `letter_count` to count the occurances of each letter
# in a string. Use a dictionary.
#
# You can iterate over a string one letter at a time using
# a for loop.
#
# for letter in "alpha":
#   print(letter)
#
# Create a dictionary with `dd = {}`. Assign values with `dd["foo"] = 1`.
# Check to see if a dictionary has a key using the `in` operator.
#
#
# Careful. Python requires that you insert a key into a dictionary
# before you try to modify it's value. If you try to access a dictionary
# at a key that hasn't been added you'll get an error and the program will
# crash. Remember to use an if statement to see if a key is "in" a dictionary
# before you try to read it!
#
# d2 = {}
# d2["foo"]
# > KeyError: 'foo'
#
# Example function call:
#
# letter_count('banana')
#
# > {'a': 3, 'b': 1, 'n': 2}

letter_dictionary = {
    "name": "andrewharrisonbantly"
}

letter_counter = {}

def letter_count(word):
    for letter in letter_dictionary[word]:
        print(letter)
        if letter in letter_counter:
            letter_counter[letter] += 1
        else:
            letter_counter[letter] = 1
    print(letter_counter)

def another_letter_count(word):
    dd = {}
    # iterate over the word
    for char in word:
        # if the char is found in the dictionary, increment it's value
        if char in dd:
            dd[char] += 1
        # otherwise add it with a value of one
        else:
            dd[char] = 1
    print(dd)

another_letter_count("google")

letter_count("name")