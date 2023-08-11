"""
Exercise 18: Replace each special symbol with # in the following string
"""
import string


def replace_special(s):
    print(f"Original string: {s}")
    res = s[::]

    # Solution 1
    # for ch in s:
    #     if ch.isdigit() or ch.isalpha() or ch == ' ':
    #         res += ch
    #     else:
    #         res += '#'

    # Solution 2
    for char in s:
        if char in string.punctuation:
            res = res.replace(char, '#')

    return res


str1 = '/*Jon is @developer & musician!!'
print(f"Modified string: {replace_special(str1)}")
