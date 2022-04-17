"""
Read an distance in kilometers and introduce her converted in miles. A formula of conversion is: M = K/1,61, being K
a distance in kilometers and M in miles.

"""

distance_in_kilometers = float(input("Write an distance in kilometers: "))
print(f"{distance_in_kilometers/1.61:.2f} miles.")

