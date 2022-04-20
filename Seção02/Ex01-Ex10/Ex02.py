"""
Read a number provided by the user. If this number is positive, calculate the square root of number. If the number is
negative, show a message saying that the number is invalid.

"""
import math

number: float = float(input("Write a number: "))
if number >= 0:
    print(f"Your square root is: {math.sqrt(number):.2f}")
else:
    print("Number is invalid!")

