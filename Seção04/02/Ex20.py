def guardar_dados(matriz: float, linha: int, coluna: int, flag1: int, flag2: int) -> float:
    try:
        for i in range(flag1, linha):
            for j in range(flag2, coluna):
                matriz[i][j] = float(input(f"Digite um número para a linha:{flag1+1} na coluna:{flag2+1}: "))
                flag2 += 1
            flag1 += 1
            flag2 = 0
        return matriz
    except ValueError as error:
        print(f"Valor errado!!!{error}")
        return guardar_dados(matriz, linha, coluna, flag1, flag2)


def soma_colunas_impares(matriz: float, linha: int, coluna: int) -> float:
    soma: float = 0
    for i in range(1, linha+1):
        for j in range(1, coluna+1):
            if j % 2 != 0:
                soma += matriz[i-1][j-1]
    return soma


def media_aritmetrica(matriz: float, linha: int, coluna: int) -> float:
    media: float = 0.0
    soma: float = 0.0
    for i in range(linha):
        for j in range(coluna):
            if j == 1 or j == 3:
                soma += matriz[i][j]
    media = soma/6
    return media


def modificar_matriz(matriz_new: float, linha: int, coluna: int) -> float:
    nova_matriz: float = [[i*0 for i in range(coluna)] for j in range(linha)]
    for i in range(linha):
        soma: float = 0
        for j in range(coluna):
            if j == 0 or j == 1:
                soma += matriz_new[i][j]
            elif j == 5:
                nova_matriz[i][j] = soma
            if j != 5:
                nova_matriz[i][j] = matriz_new[i][j]
    return nova_matriz


linha: int = 3
coluna: int = 6
matriz: float = [[i*0 for i in range(coluna)] for j in range(linha)]
matriz_new: float = guardar_dados(matriz, linha, coluna, flag1=0, flag2=0)
soma_impares: float = soma_colunas_impares(matriz_new, linha, coluna)
media: float = media_aritmetrica(matriz_new, linha, coluna)
matriz_modificada: float = modificar_matriz(matriz_new, linha, coluna)
print(f"A soma de todos os elementos das colunas impares : {soma_impares}")
print(f"A média aritmétrica dos elementos da segunda e quarta colunas: {media}")
print(f"A matriz original: ")
for listas in matriz_new:
    print(listas)
print(f"Matriz modificada: ")
for listas in matriz_modificada:
    print(listas)

