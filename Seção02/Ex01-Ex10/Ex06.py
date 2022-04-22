"""
Write a program that, receives two integer numbers show the biggest of them on the screen, so as the difference existence
between both.

"""

first_number: int = int(input("Write the first number integer: "))
second_number: int = int(input("Write the second number integer: "))
if first_number > second_number:
    print(f"First number is bigger than second number! the difference between is: {first_number - second_number} ")
elif second_number > first_number:
    print(f"Second number is bigger than first number! the difference between is: {second_number - first_number} ")
else:
    print("both are equals!")
