"""
Exercise 4: Concatenate two lists in the following order
"""

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

# Solution 1
result1 = []
for w1 in list1:
    for w2 in list2:
        result1.append(w1 + w2)

print(result1)

# Solution 2
result2 = [w1 + w2 for w1 in list1 for w2 in list2]
print(result2)