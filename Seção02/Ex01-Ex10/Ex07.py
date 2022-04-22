"""
Make a program that receives two numbers and show the biggest. If by chance, the two numbers is equals, print
the message "Same Numbers"

"""

first_number: float = float(input("Write the first number: "))
second_number: float = float(input("Write the second number: "))
if first_number > second_number:
    print(f"First number is bigger than second number! the difference between is: {first_number - second_number} ")
elif second_number > first_number:
    print(f"Second number is bigger than first number! the difference between is: {second_number - first_number} ")
else:
    print("Same Numbers!")
