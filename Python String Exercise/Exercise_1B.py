"""
Exercise 1B: Create a string made of the middle three characters
Write a program to create a new string made of the middle three characters of an input string.
"""


def middle_chars(s):
    mid = (len(s) // 2) - 1
    return s[mid:mid+3]


str1 = input('Original string: ')

print(f'Middle three chars: {middle_chars(str1)}')