"""
Implement a program that calculates a person's year of birth from their age and current year.
"""
import datetime

age: int = int(input("Write your age: "))
date_today: datetime = datetime.datetime.now()
year_now = date_today.year
print(f"Your year of birth is: {year_now - age}")