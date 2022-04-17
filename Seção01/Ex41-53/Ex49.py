"""
Write a program to read the start time (hour, minutes, seconds) and duration, in seconds, of a biological experiment.
The program should result with the new time (hour, minutes, seconds) at the end of the same.
"""
import datetime


def duration(value_in_seconds: int) -> datetime:
    if value_in_seconds > 86399:
        print("This value is very high that 86399 seconds.")
    if value_in_seconds > 60:
        minutos = (value_in_seconds) / 60 % 60
        segundos = value_in_seconds % 60
        horas = value_in_seconds / 60 / 60
        return horas, minutos, segundos
    else:
        return 0, 0, value_in_seconds


time_start: str = input("Write the star time (00:00:00) : ").split(':')
duration_seconds: int = int(input("Write the duration in seconds: "))
hora: int = (int(time_start[0]) * 60) * 60
minuto: int = int(time_start[1]) * 60
segundos: int = int(time_start[2]) + hora + minuto
duration_seconds += segundos
time_duration: datetime = duration(duration_seconds)
time_start_new: datetime = datetime.time(int(time_duration[0]), int(time_duration[1]), int(time_duration[2]))

print(f" This new time is = {time_start_new}")
