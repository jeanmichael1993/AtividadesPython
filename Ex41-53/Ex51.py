"""
Write a program that reads the x and y
coordinates of points on r2 and calculates their distance from the origin (0,0).
"""

x: float = float(input("Write value x: "))
y: float = float(input("Write value y: "))
print(f"{((x ** 2 + y ** 2) ** (1/2)):.2f}")