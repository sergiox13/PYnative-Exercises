"""
Exercise 14: Print downward Half-Pyramid Pattern with Star (asterisk)
"""

#  Solution 1
for i in range(5, 0, -1):
    print('* ' * i)

print()

#  Solution 2
for i in range(5, 0, -1):
    for j in range(i):
        print('*', end=' ')
    print()
