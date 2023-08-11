"""
Exercise 17: Find words with both alphabets and numbers
"""


def alphas_numbers(s):
    lst = s.split()
    res = []
    for item in lst:
        if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
            res.append(item)
    for el in res:
        print(el)


str1 = "Emma25 is Data scientist50 and AI Expert"
alphas_numbers(str1)