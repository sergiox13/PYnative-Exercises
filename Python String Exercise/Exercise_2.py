"""
Exercise 2: Append new string in the middle of a given string
Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
"""
def append_middle(s1, s2):
    print(f'Original strings: {s1}, {s2}')
    mid = len(s1) // 2
    new_s = s1[:mid] + s2 + s1[mid:]
    print(f'Modified str: {new_s}')

append_middle('Ault', 'Kelly')