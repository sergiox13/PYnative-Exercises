"""
Exercise 11: Reverse a given string
"""

str1 = "PYnative"

# Solution 1
print(str1[::-1])

# Solution 2
res = reversed(str1)
res = ''.join(res)
print(res)
