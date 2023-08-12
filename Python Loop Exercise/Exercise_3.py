"""
Exercise 3: Calculate the sum of all numbers from 1 to a given number
Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)
"""


n = int(input('Enter number: '))
s = 0

# Solution 1
for i in range(n + 1):
    s += i

print(f"Sum is: {s}")

# Solution 2
print(f"Sum is: {sum(range(1, n + 1))}")