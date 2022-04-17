"""
Write a program to read the dimensions of a plot (length c and width l),
as well as the price of a meter of canvas p.
Print the cost to fencing this same plot of land with canvas.
"""

c: float = float(input("Write the length of a plot: "))
l: float = float(input("Write the width of a plot: "))
p: float = float(input("Write the meter of canvas: "))
print(f"the cost is : {(c * l * p):.2f}")
