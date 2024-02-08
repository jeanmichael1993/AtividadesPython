
def guardar_dados(matriz: int, linha: int, coluna: int, count0: int, count1: int) -> int:
    try:
        for i in range(count0, linha):
            for j in range(count1, coluna):
                matriz[i][j] = int(input(f"Digite um valor para a coluna {count1+1} e linha {count0+1}: "))
                count1 += 1
            count1 = 0
            count0 += 1
        return matriz
    except ValueError as error:
        print('Valor errado!')
        return guardar_dados(matriz, linha, coluna, count0, count1)


def soma(matriz: int, linha: int, coluna: int, n: int) -> int:
    soma: int = 0
    for i in range(linha):
        for j in range(coluna):
            if i == n:
                soma += matriz[i][j]
    return soma


if __name__ == "__main__":
    try:
        linha = 7
        coluna = 6
        matriz: int = [[x for x in range(coluna)] for i in range(linha)]
        matriz_new: int = guardar_dados(matriz, linha, coluna, count0=0, count1=0)
        for i in matriz_new:
            print(i)
        n: int = int(input("Digite a linha para a soma de 1 a 7: "))
        resultado = soma(matriz_new, linha, coluna, n-1)
        print(f'A Soma dos elementos da linha {n} da matriz é : {resultado}')
    except ValueError as error:
        print('valor de N está errado!')


