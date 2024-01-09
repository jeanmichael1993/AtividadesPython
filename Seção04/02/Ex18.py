def guardar_dados(matriz: int, linha: int, coluna: int, flag1: int, flag2: int) -> int:
    try:
        for i in range(flag1, linha):
            for j in range(flag2, coluna):
                matriz[i][j] = int(input(f"Digite um valor para a linha: {flag1+1} e coluna: {flag2+1} :"))
                flag2 += 1
            flag1 += 1
            flag2 = 0
        return matriz
    except ValueError as error:
        print(f"Valor errado!! {error}")
        return guardar_dados(matriz, linha, coluna, flag1, flag2)


def soma_colunas(matriz, linha, coluna, vet: int) -> int:
    soma1: int = 0
    soma2: int = 0
    soma3: int = 0
    for i in range(linha):
        for j in range(coluna):
            if j == 0:
                soma1 += matriz[i][j]
            elif j == 1:
                soma2 += matriz[i][j]
            elif j == 2:
                soma3 += matriz[i][j]
    return soma1, soma2, soma3


linha: int = 3
coluna: int = 3
matriz: int = [[i*0 for i in range(3)] for j in range(3)]
nova_matriz: int = guardar_dados(matriz, linha, coluna, flag1=0, flag2=0)
vetor: int = soma_colunas(nova_matriz,linha, coluna, [])
print(vetor)

