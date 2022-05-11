"""
16 - Usando switch, escreve um programa que leia um numero inteiro entre 1 e 12 e imprima o mês
correspondente a este numero. Isto é, janeiro se 1, fevereiro se 2, e assim por diante.

"""

number_int: int = int(input("Write a number between 1 and 12: "))
switch = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}
print(switch.get(number_int, "Number Invalid!"))

