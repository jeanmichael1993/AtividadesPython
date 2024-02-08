
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


if __name__ == "__main__":
    matriz: int = [[x for x in range(4)] for i in range(4)]
    nova_matriz = guardar_dados(matriz, linha=4, coluna=4, count0=0, count1=0)
    soma: int = []
    [[soma.append(i) for i in j if i > 10 ] for j in matriz]
    print(f'A quantidade de números na matriz maior que 10 é : {len(soma)}')

