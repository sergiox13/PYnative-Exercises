"""
Exercise 3: Turn every item of a list into its square
Given a list of numbers. write a program to turn every item of a list into its square.
"""

numbers = [1, 2, 3, 4, 5, 6, 7]
square_list = [n * n for n in numbers]
print(f"Squares: {square_list}")