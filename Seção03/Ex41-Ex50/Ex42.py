import math
cond: bool = True
while cond:
    try:
        valor: int = int(input("Digite um valor: "))
        if valor <= 0:
            print('Valor invalido!')
            cond = False
        else:
            print(f'O quadrado desse número é : {valor ** 2}')
            print(f'O cubo desse número é : {valor ** 3}')
            print(f'A raiz quadrada desse número é : {math.sqrt(valor):.2f}')

    except ValueError as error:
        print(error)