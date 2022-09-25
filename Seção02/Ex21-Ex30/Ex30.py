"""
Make a program that receive three numbers and show in ascending order.


"""

num1: int = int(input("Write the first number:"))
num2: int = int(input("Write the second number:"))
num3: int = int(input("Write the third number:"))
listNum: int = [num1, num2, num3]
listNum.sort(reverse=False)
listNew = [x for x in listNum]
print(listNew)
