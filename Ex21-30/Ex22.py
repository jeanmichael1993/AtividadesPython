"""
Read a value of length in yards and introduce converted in meters. The formula of conversion is:
M = 0.91 * J, being J the length in yards and M the length in meters.
"""

value_of_length_in_yards: float = float(input("Write the value of length in yards: "))
print(f'{0.91 * value_of_length_in_yards} length in meters.')

