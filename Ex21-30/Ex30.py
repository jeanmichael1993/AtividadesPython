"""
Read a value in Real and the quotation of dollar. Then, print the value corresponding in dollars.

"""
print("Write the value in Real: ")
value_in_real: float = float(input())
print("Write the value in Dollar: ")
value_in_dollar: float = float(input())
print(f'The value {value_in_real:.2f} Real in dollars is {value_in_dollar * value_in_real:.2f}')
