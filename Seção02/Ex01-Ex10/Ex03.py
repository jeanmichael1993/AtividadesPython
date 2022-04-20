"""
Read a number real. If the number is positive print the square root, otherwise, print the number squared.

"""
import math

number: int = int(input("Write a number real: "))
if number >= 0:
    print(f"Number is positive, its square root is {math.sqrt(number):.2f}")
else:
    print(f"Number is negative, its number squared is {number ** 2}")

