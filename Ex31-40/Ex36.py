"""
Read the height and the radius the a circular cylinder and print the cylinder volume. The volume of a circular cylinder
is calculate for: V = PI * radius ** 2 * height, being PI = 3.141592.

"""
PI: float = 3.141592
height_circular_cylinder: float = float(input("Write the value of height the a circular cylinder: "))
radius_circular_cylinder: float = float(input("Write the value of radius the a circular cylinder: "))
print(f"Your volume of a circular cylinder is: {(PI * (radius_circular_cylinder ** 2) * height_circular_cylinder):.2f} ")
