def obter_valor() -> int:
    try:
        valor_n: int = int(input("Digite o valor de N: "))
        if valor_n <= 0:
            print("Valor incorreto!!!")
            return obter_valor()
        return valor_n
    except ValueError as error:
        print(error)
        return obter_valor()


def imprimir_tri_floyd(x: int):
    teste: int = 1
    for i in range(1, x+1):
        for t in range(i):
            print(teste, end=' ')
            teste += 1
        print(end='\n')


imprimir_tri_floyd(obter_valor())