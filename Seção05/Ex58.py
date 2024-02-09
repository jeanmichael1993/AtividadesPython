
def guardar_dados(linha: int, coluna: int, count0: int, count1: int) -> int:
    try:
        matriz: int = [[x for x in range(coluna)] for i in range(linha)]
        for i in range(count0, linha):
            for j in range(count1, coluna):
                matriz[i][j] = int(input(f"Digite um valor para a coluna {count1+1} e linha {count0+1}: "))
                count1 += 1
            count1 = 0
            count0 += 1
        return matriz
    except ValueError as error:
        print('Valor errado!')
        return guardar_dados(linha, coluna, count0, count1)


def soma(matriz_A: int,matriz_B: int, linha: int, coluna: int) -> int:
    soma: int = 0
    matriz_new: int = [[0 for x in range(coluna)] for i in range(linha)]
    for i in range(linha):
        for j in range(coluna):
            for y in range(coluna):
                matriz_new[i][j] += matriz_A[i][y] * matriz_B[y][j]

    return matriz_new


if __name__ == "__main__":
    try:
        linha = 2
        coluna = 2

        matriz_A: int = guardar_dados(linha, coluna, count0=0, count1=0)
        matriz_B: int = guardar_dados(linha, coluna, count0=0, count1=0)
        for i in matriz_A:
            print(i)
        print('------------------------------')
        for i in matriz_B:
            print(i)
        resultado = soma(matriz_A, matriz_B, linha, coluna)
        print('--------------------------------')
        for i in resultado:
            print(i)
    except ValueError as error:
        print('valor de N está errado!')


