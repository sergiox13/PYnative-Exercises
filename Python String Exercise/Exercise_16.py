"""
Exercise 16: Removal all characters from a string except integers
"""


def only_integers(s):
    print(f"Original string: {s}")
    ints = [i for i in s if i.isdigit()]
    return ''.join(ints)


str1 = 'I am 25 years and 10 months old'
print(f'Only integers: {only_integers(str1)}')