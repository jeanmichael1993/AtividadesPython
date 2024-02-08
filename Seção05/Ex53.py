
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


def soma(matriz: int, linha: int, coluna: int) -> int:
    flag: int = 0
    for i in range(linha):
        for j in range(coluna):
            if i == j:
                if i != 0 and j != 0:
                    if matriz[i][j] == matriz[i-1][j-1]:
                        flag = 1
                    else:
                        return 0
    return flag


if __name__ == "__main__":
    try:
        n: int = int(input("Digite o valor de N: "))
        linha = coluna = n
        matriz: int = [[x for x in range(coluna)] for i in range(linha)]
        matriz_new: int = guardar_dados(matriz, linha, coluna, count0=0, count1=0)
        for i in matriz_new:
            print(i)
        resultado = soma(matriz_new, linha, coluna)
        print(f'A respostas é {'Não é matriz identidade' if resultado == 0 else 'É matriz identidade'}')
    except ValueError as error:
        print('valor de N está errado!')


