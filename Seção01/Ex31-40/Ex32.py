"""
Read a number integer and print the sum of successor of its triple as the predecessor of its double.

"""

number: int = int(input("Write a value integer: "))
print(f"The sum of successor and its predecessor is : {((number+1)*3) + ((number-1)*2)}")

