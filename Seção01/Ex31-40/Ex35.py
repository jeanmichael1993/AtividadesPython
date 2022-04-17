"""
Are A and B the catheters of a triangle, where the hypotenuse is obtained by the equation:
hypotenuse = root(a**2+b**2).Make a program that receives the values of A and B and calculate
the hypotenuse value trough the equation. Print the result of this operation.

"""
import math

A: float = float(input("Write a value of A: "))
B: float = float(input("write a value of B: "))

hypotenuse = math.sqrt(A ** 2 + B ** 2)

print(f"Its result of hypotenuse is : {hypotenuse:.2f}")
