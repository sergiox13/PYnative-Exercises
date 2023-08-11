"""
Exercise 5: Count all letters, digits, and special symbols from a given string
"""


def count_chars(s):
    print(f"Original string: {s}")
    chars = ''
    digits = ''
    symbols = ''
    for ch in s:
        if ch.isalpha():
            chars += ch
        elif ch.isnumeric():
            digits += ch
        else:
            symbols += ch
    print(
        f'Chars: {len(chars)}\n' 
        f'Digits: {len(digits)}\n'
        f'Symbols: {len(symbols)}'
    )


str1 = "P@#yn26at^&i5ve"
count_chars(str1)