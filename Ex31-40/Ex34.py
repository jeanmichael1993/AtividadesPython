"""
Read the radius value of a circle and calculate and print the circle area corresponding.
The circle area is PI * radius**2, being PI = 3.141592

"""
PI: float = 3.141592
radius_value_of_circle: float = float(input("Write a radius value of a circle: "))
print(f"Its circle area corresponding is: {(PI * (radius_value_of_circle**2)):.2f}")

