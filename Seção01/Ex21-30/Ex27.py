"""
Read a value of area in hectares and introduce converted in meters square. The formula of conversion is:
M = H * 10000, being M the area in meters square and H the area in hectares.

"""

value_of_area_in_hectares: float = float(input("Write the value of area in hectares: "))
print(f'The value converted in meters square is: {value_of_area_in_hectares * 10000:.2f}')
