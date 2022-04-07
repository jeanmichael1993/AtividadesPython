"""
Make a program that read a value of a product and print the discounted value, given that the discount was 12%

"""
discount: float = 0.12
value_of_product: float = float(input("Write the value of product: "))
print(f"The discounted value is: {(value_of_product - (value_of_product * discount)):.2f}")
