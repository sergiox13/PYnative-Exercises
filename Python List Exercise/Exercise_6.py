"""
Exercise 6: Remove empty strings from the list of strings
"""

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# Solution 1
res = [x for x in list1 if x]
print(res)

# Solution 2
res1 = list(filter(None, list1))
print(res1)
