"""
Read an integer value in seconds, and print in hours, minutes and seconds.
"""
import datetime

value_in_seconds: int = int(input("Write an integer value in seconds: "))
if value_in_seconds > 86399:
    print("This value is very high that 86399 seconds.")
if value_in_seconds > 60:
    minutos = (value_in_seconds) / 60 % 60
    segundos = value_in_seconds % 60
    horas = value_in_seconds / 60 / 60
    date = datetime.time(int(horas),int(minutos),int(segundos))
    print(f"{date}")
else:
    print(f"00:00:{value_in_seconds}")


