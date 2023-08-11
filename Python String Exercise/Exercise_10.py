"""
Exercise 10: Write a program to count occurrences of all characters within a string
"""


def count_occur(s):
    result = {}
    for ch in s:
        result[ch] = s.count(ch)
    return result


str1 = "Apple"
print(count_occur(str1))
