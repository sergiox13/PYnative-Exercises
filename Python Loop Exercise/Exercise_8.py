"""
Exercise 8: Print list in reverse order using a loop
"""

# Solution 1
list1 = [10, 20, 30, 40, 50]
size = len(list1) - 1
for i in range(size, -1, -1):
    print(list1[i])

print()
# Solution 2

for el in reversed(list1):
    print(el)