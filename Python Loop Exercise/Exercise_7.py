"""
Exercise 7: Print the following pattern
Write a program to use for loop to print the following reverse number pattern

5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
"""

# Solution 1
for i in range(5, 0, -1):
    for j in range(i):
        print(i-j, end=' ')
    print()

# Solution 2
n = 5
m = 5
for i in range(0, n+1):
    for j in range(m - i, 0, -1):
        print(j, end=' ')
    print()