"""
Read a value of volume in meters cubic m3 and introduce her converted in liters. A formula of conversion is:
L = 1000 * M, being L the volume in liters and M the volume in meters cubic

"""

volume_in_meters_cubic = float(input("Write a value of volume in meters cubic m3: "))
print(f"{1000 * volume_in_meters_cubic:.2f} liters")

