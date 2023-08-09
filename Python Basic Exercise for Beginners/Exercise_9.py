"""
Exercise 9: Check Palindrome Number
Write a program to check if the given number is a palindrome number.

A palindrome number is a number that is same after reverse. For example 545, is the palindrome numbers
"""

def is_palindrome(n):
    temp = str(n)

    if temp == temp[::-1]:
        return 'Yes. Given number is palindrome number'
    return 'No. Given number is not palindrome number'


n = int(input('Original number: '))
result = is_palindrome(n)
print(result)
