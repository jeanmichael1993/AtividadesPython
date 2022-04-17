"""
Make a program to convert an uppercase letter to a lowercase letter. Use the ASCII table to solve the problem.
"""

letter: str = input("Write a letter: ").upper()
num_letter = ord(letter)
print(chr(num_letter + 32))

