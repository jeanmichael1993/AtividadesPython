"""
a company hires a plumber at R$ 30.00 per day. Make a program that asks for the number of days worked by the
plumber and prints the net amount that must be paid, knowing that 8% is deducted for income tax.
"""

tax: float = 0.08
per_day: float = 30
days_worked: int = int(input("Write number of days worked: "))
print(f"The net amount is: {(days_worked * per_day - ((days_worked * per_day) * tax)):.2f}")
