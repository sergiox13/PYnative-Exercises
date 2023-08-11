"""
Exercise 15: Remove special symbols / punctuation from a string
"""

def remove_special(s):
    lst = [el for el in s if el.isalpha()]
    return lst


str1 = "/*Jon is @developer & musician"
print(remove_special((str1)))