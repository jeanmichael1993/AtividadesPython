def guardar_dados() -> int:
    numero: int = int(input("Digite um numero: "))
    return numero


def contar(list: int ):
    soma: int = 0
    for lista in list:
        for x in lista:
            if x >= 0:
                soma += 1
    return print(soma)


tabuleiro = [[guardar_dados() for numero in range(4)] for valor in range(4)]
counter: int = [[numero for numero in lista if numero > 10] for lista in tabuleiro]
contar(counter)
