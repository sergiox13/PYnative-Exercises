"""
Exercise 7: String characters balance Test
Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. The character’s position doesn’t matter.
"""

def is_balanced(s1, s2):
    temp = ''
    for ch in s1:
        if (ch in s2) and (ch not in temp):
            temp += ch
    if len(s1) == len(temp):
        return True
    return False



str1 = "Yn"
str2 = "PYnative"
print(is_balanced(str1, str2))

str3 = "Ynf"
str4 = "PYnative"
print(is_balanced(str3, str4))