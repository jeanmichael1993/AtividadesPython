"""

Read a angle in radians and introduce her converted in degrees. A formula of conversion is :
G = R * 180/PI, being G the angle in degrees and R in radians and PI = 3.14.

"""
import math

angle_in_radias = float(input("Write an angle in radians : "))
print(f"{angle_in_radias * 180/math.pi:.2f} degrees")
