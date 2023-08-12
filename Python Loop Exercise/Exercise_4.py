"""
Exercise 4: Write a program to print multiplication table of a given number
For example, num = 2 so the output should be
"""

n = int(input('Enter a number: '))

print(f"Multiplication table for {n}")
for i in range(1, 11):
    print(i * n)