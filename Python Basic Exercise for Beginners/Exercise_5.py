"""
Exercise 5: Check if the first and last number of a list is the same
Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.
"""


def is_the_same(lst):
    print(f'Given list: {lst}')

    if lst[0] == lst[-1]:
        return True

    return False


lst1 = [10, 20, 30, 40, 10]
print(f'Result is {is_the_same(lst1)}')

lst2 = [75, 65, 35, 75, 30]
print(f'Result is {is_the_same(lst2)}')
