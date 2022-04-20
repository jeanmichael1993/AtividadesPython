"""
Make a program that to receive two numbers and show which is bigger.

"""
number_one: float = float(input("Write the first number: "))
number_two: float = float(input("Write the second number: "))
if number_one > number_two:
    print(f"{number_one} is bigger than {number_two}")
elif number_two > number_one:
    print(f"{number_two} is bigger than {number_one}.")
else:
    print("both numbers are equals!")

