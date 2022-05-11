"""
Write a program that read a number greater than zero and return, on the screen, the sum of all its digits
for example, to the number 251 will correspond to the value 8 ( 2 + 5 + 1). If the number read is not greater than
zero, the program ends with the message "invalid number".

"""

number: str = input("Write a number greater que zero: ")
if int(number) == 0:
    print("Invalid Number")
else:
    sum_number: int = 0
    for x in number:
        sum_number += int(x)

    print(f'The sum of all digits is : {sum_number}')
