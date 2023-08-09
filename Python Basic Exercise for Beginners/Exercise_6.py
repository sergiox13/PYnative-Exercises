"""
Exercise 6: Display numbers divisible by 5 from a list
Iterate the given list of numbers and print only those numbers which are divisible by 5
"""

nums = [10, 20, 33, 46, 55]
print("Given list:", nums)
print('Divisible by 5:')
for n in nums:
    if n % 5 == 0:
        print(n)