"""
Read a value of dough in pounds and introduce converted in kilograms.The formula of conversion is:
K = L * 0.45 , being K a dough in kilograms and L a dough in pounds

"""

value_of_dough: float = float(input("Write value of dough in pounds: "))
print(f'{value_of_dough*0.45:.2f} pounds.')

