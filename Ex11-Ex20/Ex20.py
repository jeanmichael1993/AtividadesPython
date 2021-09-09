"""
Read a value of dough in Kilograms and introduce in pounds. A formula of conversion is:
L = K/0.45, being K a dough in kilograms and L a dough in pounds.
"""

value_of_dough = float(input("Write value of dough: "))
print(f"{value_of_dough/0.45:.2f} pounds.")

