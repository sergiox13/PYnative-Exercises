"""
Exercise 13: Split a string on hyphens
Write a program to split a given string on hyphens and display each substring.
"""


def split_string(s):
    print(f'Original string: {s}')
    print('Result:\n')

    for word in s.split('-'):
        print(word)


str1 = 'Emma-is-a-data-scientist'
split_string(str1)
