def exponent(base, exp):
    return base ** exp

base = int(input('Base: '))
exp = int(input('Exponent: '))

result = exponent(base, exp)
times = (str(base) + "*") * exp

print(
    f'{base} raises to the power of {exp} is: {result}\n'
    f'i.e. {times[:-1]} = {result}'
)
