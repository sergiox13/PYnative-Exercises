"""
Exercise 2: Print the sum of the current number and the previous number
Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.
"""

s = 0
prev_num = 0

for i in range(10):
    s = prev_num + i
    print(f'Current Number {i} Previous Number {prev_num} Sum: {s}')
    prev_num = i