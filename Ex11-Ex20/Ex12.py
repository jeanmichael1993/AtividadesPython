"""
Read an distance in miles(meters per second) and introduce her converted in Kilometers. A formula of
conversion is : K = 1,61 * M, being K a distance in kilometers and M in miles.

"""

distance_in_miles = float(input("Write an distance in miles: "))
print(f"{1.61 * distance_in_miles} kilometers.")