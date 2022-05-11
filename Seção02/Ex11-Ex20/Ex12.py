"""
Read a number integer. If the number read is negative, write the message "Number invalid". If the number is positive
, calculate the digit of this number.

"""

number_integer: int = int(input("Write a number integer: "))
if number_integer < 0:
    print("Number Invalid!")
else:
    quantity: int = 0
    number_stop: int = number_integer
    while number_stop > 1:
        number_stop: int = int(number_stop / 2)
        quantity += 1
        print(f"2 ** {quantity}")

