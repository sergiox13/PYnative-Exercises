"""
Exercise 3: Create a new string made of the first, middle, and last characters of each input string
Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.
"""


def modified_str(s1, s2):
    print(f'Original strings: {s1}, {s2}')
    mid_s1 = len(s1) // 2
    mid_s2 = len(s2) // 2
    mid = s1[mid_s1] + s2[mid_s2]
    new_s = s1[0] + s2[0] + mid + s1[-1] + s2[-1]
    print(f'Modified string: {new_s}')


modified_str('America', 'Japan')