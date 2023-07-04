r1: int = 0
r2: int = 0
r: int = None
while r != 0:
    try:
        r1 = int(input("Digite o valor de R1: "))
        r2 = int(input("Digite o valor de R2: "))
        r = (r1 * r2) / (r1 + r2)
    except ValueError as error:
        print(error)
    except ZeroDivisionError as erro2:
        print(erro2)
        