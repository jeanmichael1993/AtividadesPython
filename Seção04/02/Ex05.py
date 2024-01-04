def guardar_valores(x, j) -> int:
    try:
        numero: int = int(input(f"Digite um valor da posição {x} na linha {j}º: "))
        return numero
    except ValueError as error:
        print(f"Valor errado!{error}")
        return guardar_valores(x, j)


def guardar_valor_x() -> int:
    try:
        numero: int = int(input(f"Digite o valor de X: "))
        return numero
    except ValueError as error:
        print(f"Valor errado!{error}")
        return guardar_valor_x()


matriz: int = [[guardar_valores(i, j) for i in range(1, 6)] for j in range(1, 6)]
valor_x: int = guardar_valor_x()
posicao: int = 0
flag: int = 0
linha: int = 0
for lista in matriz:
    for x in lista:
        if x == valor_x:
            flag = 1
            posicao = lista.index(x)
            linha = matriz.index(lista)

if flag == 1:
    print(f"O valor está na linha:{linha+1} e na posição: {posicao+1}!")
else:a
    print("Valor não encontrado na matriz!")
