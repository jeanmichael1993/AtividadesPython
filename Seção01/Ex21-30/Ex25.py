"""
Read a value of area in acres and introduce converted in meters square m2. The formula of conversion is:
M = A * 4048.58, being M the area in meters square and A the area in acres.
"""

value_of_area_in_acres: float = float(input("Write the value of area in acres: "))
print(f'The value of meters square is: {value_of_area_in_acres * 4048.58:.2f}')