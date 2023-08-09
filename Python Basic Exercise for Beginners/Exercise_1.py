"""
Exercise 1: Calculate the multiplication and sum of two numbers
Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.
"""

n1 = int(input('n1: '))
n2 = int(input('n1: '))

product = n1 * n2

if product <= 1000:
    print(f'The result is {product}')
else:
    print(f'The result is {n1 + n2}')