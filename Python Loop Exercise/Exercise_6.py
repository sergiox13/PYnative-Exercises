"""
Exercise 6: Count the total number of digits in a number
Write a program to count the total number of digits in a number using a while loop.

For example, the number is 75869, so the output should be 5.
"""

n = int(input('Enter a number: '))

# Solution 1
print(f"Total digits: {len(str(n))}")

# Solution 2
count = 0
while n > 0:
    n = n // 10
    count += 1

print(f"Total digits: {count}")


