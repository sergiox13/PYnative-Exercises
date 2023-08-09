"""
Exercise 3: Print characters from a string that are present at an even index number
Write a program to accept a string from the user and display characters that are present at an even index number.

For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.
"""

s = input('Enter text: ')

print(f'Original string: {s}')
print('Printing only even index chars:')

#Solution 1
for i in range(0, len(s), 2):
    print(s[i])

#Solution 2
print(s[::2])