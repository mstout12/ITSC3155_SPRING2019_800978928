# Python Activtiy
# 
# Fill in the code for the functions below. 
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.

# Part A. starts_with
# Define a function starts_with(s, char) that takes a string and a character
# and returns true if the string starts with that character and false otherwise. 
def starts_with(s, char):
  if (len(s) != 0 and len(char) != 0):
    return s[0] == char
  if (len(s) == 0 and len(char) == 0):
    return True
  return 0
  
  return

# Part B. starts_with_vowel
# Define a function starts_with_vowel(s) that takes a string and
# returns true if the string starts with a vowel and false otherwise. 
# For our purposes, a consonant is any letter other than A, E, I, O, U)
# Your solution should work for both upper and lower cases 
def starts_with_vowel(s):
  if (len(s) != 0):
    if s[0].lower() == 'a' or 'e' or 'i' or 'o' or 'u':
      return True
    else:
      return False
  return 0

# Part C. max_min_sum
# Define a function max_min_sum(arr) that takes an array and returns the sum
# of the largest element and the smallest element of the array.
# For an empty array it should return zero
# For an array with just one element, it should return that element
def max_min_sum(arr):
  if len(arr) == 0:
    return 0
  if len(arr) == 1:
    return arr[0]
  maxNum = max(arr)
  minNum = min(arr)
  return maxNum + minNum