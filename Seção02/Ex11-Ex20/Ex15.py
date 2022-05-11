"""
Using switch, write a program that reads an entire number between 1 and 7 and print the day of the
week corresponding to this number. That is, Sunday if 1, Monday if 2, and so on.
"""

number_int: int = int(input("Write a number between 1 and 7: "))
switch = {
    1: 'Sunday',
    2: 'Monday',
    3: 'Tuesday',
    4: 'Wednesday',
    5: 'Thursday',
    6: 'Friday',
    7: 'Saturday'
}
print(switch.get(number_int, "Number Invalid!"))

