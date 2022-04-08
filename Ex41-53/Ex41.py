"""
Make a program that read the value of work time and number of worked hours in month. Print the amount to be paid
to employee, adding 10% about the value calculated.
"""

value_of_work_time: float = float(input("Write value of work time: "))
numbers_of_worked_hours_in_month: int = int(input("Write the numbers of worked hours in month: "))
print(f"{(value_of_work_time * numbers_of_worked_hours_in_month + ((value_of_work_time*numbers_of_worked_hours_in_month)* 0.10)):.2f}")
