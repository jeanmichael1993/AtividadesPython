"""
Read three values and introduce as result of sum of square of the three read values.

"""

number = []
for x in range(3):
    number.append(int(input(f"Write the {x+1}º value: ")))

print(sum([x * 2 for x in number]))

