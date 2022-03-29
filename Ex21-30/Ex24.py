"""
Read a value of area in meters square m2 and introduce converted in acres. The formula of conversion is:
A = M * 0,000247, being M the area in meters square and A the area in acres.

"""

area_in_meters_square: float = float(input("Write the value of area in meters square: "))
print(f'The value converted in acres is {area_in_meters_square * 0.000247:.2f}')