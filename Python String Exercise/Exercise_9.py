"""
Exercise 9: Calculate the sum and average of the digits present in a string
Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters.
"""


def digits_avg(s):
    print(f"Original string: {s}")
    digits = [int(i) for i in s if i.isdigit()]
    print(
        f"Sum is: {sum(digits)}\n"
        f"Avgerage: {sum(digits) / len(digits)}"
    )


str1 = "PYnative29@#8496"

digits_avg(str1)