"""
Exercise 14: Remove empty strings from a list of strings
"""


def remove_empty(lst):
    print(f"Original list: {lst}")
    return [el for el in lst if el]


str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
print(f"Modified list: {remove_empty(str_list)}")
