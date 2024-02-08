
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
    soma: int = 0
    for i in range(linha):
        for j in range(coluna):
            if i < j:
                soma += matriz[i][j]
    return soma


if __name__ == "__main__":
    linha: int = 3
    coluna: int = 3
    matriz: int = [[x for x in range(coluna)] for i in range(linha)]
    resultado = soma(guardar_dados(matriz, linha, coluna, count0=0, count1=0), linha, coluna)
    print(f'A soma dos números na matriz acima da diagonal principal é : {resultado}')

