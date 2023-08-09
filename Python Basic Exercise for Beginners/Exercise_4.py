"""
Exercise 4: Remove first n characters from a string
Write a program to remove characters from a string starting from zero up to n and return a new string.

For example:

remove_chars("pynative", 4) so output must be tive. Here we need to remove the first four characters from a string.
remove_chars("pynative", 2) so output must be native. Here we need to remove the first two characters from a string.
Note: n must be less than the length of the string.
"""

def remove_chars(s, n):
    return s[n:]

s = input('Enter text: ')
n = int(input('Enter num: '))

result = remove_chars(s, n)
print(f"Original string: '{s}'; Modified string: '{result}'")