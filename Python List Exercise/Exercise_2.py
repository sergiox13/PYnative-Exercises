"""
Exercise 2: Concatenate two lists index-wise
Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.
"""

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

# Solution 1
list3= []
for i, j in list(zip(list1, list2)):
    list3.append(i + j)
print(f"Result: {list3}")

# Solution 4
list4 = [i + j for i, j in zip(list1, list2)]
print(f"Result: {list4}")
