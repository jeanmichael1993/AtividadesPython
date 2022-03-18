"""
Read a value of length in meters and introduce converted in yards. The formula of conversion is:
J = M/0.91, being J the length in yards and M the length in meters.
"""

value_of_length_in_meters: float = float(input("Write the value of length in meters: "))
print(f'{value_of_length_in_meters/0.91:.2f} length in yards')
