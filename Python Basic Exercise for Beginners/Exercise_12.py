"""
Exercise 12: Calculate income tax for the given income by adhering to the below rules.
For example, suppose the taxable income is 45000 the income tax payable is
10000*0% + 10000*10%  + 25000*20% = $6000.
"""

income = int(input('Income: '))
first_inc = 0.0
second_inc = 10000 * 0.1
remain_inc = (income - 20000) * 0.2
tax = first_inc + second_inc + remain_inc

print(f'${tax}')

