"""
Exercise 8: Print the following pattern
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""

for col in range(1, 6):
    for row in range(col):
        print(col, end='')
    print()