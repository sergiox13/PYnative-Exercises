"""
Exercise 6: Create a mixed String using the following rules
Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.
"""

def modify_str(s1, s2):
    res1 = s1[0] + s2[-1]
    res2 = s1[1] + s2[1]
    res3 = s1[-1] + s2[0]
    print(res1 + res2 + res3)


str1 = "Abc"
str2 = "Xyz"

modify_str(str1, str2)  # AzbycX
