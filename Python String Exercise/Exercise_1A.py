"""
Exercise 1A: Create a string made of the first, middle and last character
Write a program to create a new string made of an input string’s first, middle, and last character.
"""
s = input('Original string: ')
middle = s[len(s) // 2]
print(f'New string: {s[0] + middle + s[-1]}')