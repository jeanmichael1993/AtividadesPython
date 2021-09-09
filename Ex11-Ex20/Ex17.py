"""

Read a value of length in centimeters e introduce her converted in inches.
A formula of conversion é : P  = C/2,54 , being C the length in centimeters and P the length in inches .

"""

value_of_length_centimeters = float(input("Write value of length in centimeters:  "))
print(f"{value_of_length_centimeters/2.54:.2f} inches.")

