"""
Make a program that read a number and, if it is positive, calculate and show:
* The number typed squared
* The Square root of the number typed

"""
import math

number: float = float(input("Write a number: "))
if number >= 0:
    print(f"The number squared : {(number ** 2):.2f}")
    print(f"The square root of the number typed: {math.sqrt(number):.2f}")
else:
    print("This number is invalid!")

