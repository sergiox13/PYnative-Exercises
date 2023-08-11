"""
Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
Write a program to find all occurrences of “USA” in a given string ignoring the case.
"""

str1 = "Welcome to USA. usa awesome, isn't it?"
sub_str = 'USA'

result = str1.lower().count(sub_str.lower())
print(f"The {sub_str} count is: {result}")