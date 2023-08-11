"""
Exercise 4: Arrange string characters such that lowercase letters should come first
Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.
"""

#  Solution 1
def lower_first(s):
    print(f'Original string: {s}')
    lower_str = ''
    upper_str = ''
    for ch in s:
        if ch.islower():
            lower_str += ch
        else:
            upper_str += ch
    print(lower_str + upper_str)


#  Solution 2
def lower_first1(s):
    lower_first = ''.join([ch for ch in s if ch.islower()])
    upper_first = ''.join([ch for ch in s if ch.isupper()])
    print(lower_first + upper_first)


str1 = 'PyNaTive'
lower_first(str1)
lower_first1(str1)


