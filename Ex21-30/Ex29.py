"""
Read four notes, calculate the arithmetic mean and print the result.

"""

res: float = []
for x in range(4):
    res.append(float(input(f'Write the {x + 1}º note:')))

print(f'{sum(res)/4} is the result of arithmetic mean!')
