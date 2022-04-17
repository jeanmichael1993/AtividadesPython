"""
Read a value of area in meters square and introduce converted in hectares. The formula of conversion is:
H = M * 0.0001, begin M the area in meters square and H the area in hectares.

"""

value_of_area_in_meters: float = float(input("Write the value of area in meters: "))
print(f'The value in hectares is: {value_of_area_in_meters * 0.0001:.2f}')
