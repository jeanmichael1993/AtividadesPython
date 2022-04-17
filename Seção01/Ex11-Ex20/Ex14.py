"""
Read an angle in degrees and introduce her converted in radians. A formula of conversion is:
R = G * PI/180, being G the angle in degrees and R in radians and PI = 3.14.

"""

angle_in_degress = float(input("Write an angle is degrees: "))
print(f"{angle_in_degress * 3.14 / 180 :.2f} radians.")