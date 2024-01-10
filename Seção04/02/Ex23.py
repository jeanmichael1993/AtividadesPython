def guardar_dados(matriz: int, linha: int, coluna: int, flag1, flag2, flag3) -> int:
    try:
        for i in range(flag1, linha):
            for j in range(flag2, coluna):
                matriz[i][j] = int(input(f"Digite o valor da matriz:{flag3} na linha: {flag1+1} e da coluna: {flag2+1}:  "))
                flag2 += 1
            flag1 += 1
            flag2 = 0
        return matriz
    except ValueError as error:
        print(f"Valor errado!{error}")
        return guardar_dados(matriz, linha, coluna, flag1, flag2, flag3)


def calcular(matrizA: int, linha: int, coluna: int) -> float:
    matrizB: float = [[i*0 for i in range(coluna)] for j in range(linha)]
    for i in range(linha):
        for j in range(coluna):
            matrizB[i][j] = matrizA[i][j]**2
    return matrizB


linha: int = 3
coluna: int = 3
matrizA: float = guardar_dados([[i*0 for i in range(coluna)] for j in range(linha)], linha, coluna, flag1=0, flag2=0, flag3=1)
nova_matriz: float = calcular(matrizA, linha, coluna)

for listas in matrizA:
    print(listas)
print("\n")
for listas in nova_matriz:
    print(listas)

    