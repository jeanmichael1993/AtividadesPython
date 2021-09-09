"""

Read a value of length in inches and introduce her converted in centimeters. A formula of conversion is:
 C = P * 2,54 , being C the length in centimeters and P the length in inches.
"""

length_in_inches = float(input("Write a value of lenght in inches: "))
print(f"{length_in_inches * 2.54:.2f} length in centimeters. ")