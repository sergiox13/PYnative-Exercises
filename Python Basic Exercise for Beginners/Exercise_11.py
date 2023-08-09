"""
Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.
"""

n = int(input('Enter a num:'))

while n > 0:
    d = n % 10
    n = n // 10
    print(d, end=' ')
