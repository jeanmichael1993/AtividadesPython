"""
Make a program that receives the height and gender of a person and calculate and
show your ideal weight, using the following formulas (where h corresponds to height):

*Men : (72.7 * h) - 58
*Women: (62,1 * h) - 44.7
"""

height: float = float(input("Write the height: "))
gender: str = input("Write the gender: ")
if gender == "Man":
    print(f"Your ideal weight is: {((72.7 * height)-58):.2f}")
elif gender == "Woman":
    print(f"Your ideal weight is: {((62.1 * height) - 44.7):.2f}")
else:
    print("Gender incorrect!")

