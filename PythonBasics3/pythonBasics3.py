# Python Activtiy
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.

# import regular expression module
import re


# # Part A. starts_with_number
# Define a function starts_with_number(s) that takes a string and returns true
# if it starts with a number and false otherwise.
# (For our purposes, a number is any character that is 0,1,2,3,4,5,6,7,8, or 9.)
# Note: Be sure to use RegEx!
def starts_with_number(s):
    if (len(s) != 0):
        if (re.search('^[0-9]', s)):
            return True
    return False


# # Part B. starts_with_consonant
# Define a function starts_with_consonant(s) that takes a string and returns true
# if it starts with a consonant and false otherwise.
# (For our purposes, a consonant is any letter other than A, E, I, O, U.)
# Note: Be sure to use RegEx and it works for both upper and lower case and for nonletters!
def starts_with_consonant(s):
    if re.search('^[0-9]', s):
        return False
    if len(s) != 0:
        if re.search('^[aeiouAEIOU]', s):
            return False
    return True


# Part C. binary_multiple_of_4
# define a method binary_multiple_of_4(s) that takes a string and returns true
# if the string represents a binary number that is a multiple of 4.
# Note: Be sure it returns false if the string is not a valid binary number!
# Hint: Use regular expressions to match for the pattern of a binary number that is a multiple of 4.
def binary_multiple_of_4(s):
    if len(s) != 0:
        if len(s) % 4 == 0 and re.search('^[01]*00$', s):
            return True
    return False
