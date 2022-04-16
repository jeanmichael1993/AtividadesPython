"""

Write a program that reads a three-digit positive integer (from 100 to 999).
 Generate another number formed by the inverted digits of the number read.

"""

three_digit: str = input("Write a three-digit positive interger (from 100 to 999): ")
print(three_digit[::-1])
