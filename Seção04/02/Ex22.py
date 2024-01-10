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


def calcular(matriz1: int, matriz2: int, linha: int, coluna: int) -> float:
    matrizC: float = [[i*0 for i in range(coluna)] for j in range(linha)]
    for i in range(linha):
        for j in range(coluna):
            matrizC[i][j] = matriz1[i][j] * matriz2[i][j]
    return matrizC



linha: int = 3
coluna: int = 3
matriz1: float = guardar_dados([[i*0 for i in range(coluna)] for j in range(linha)], linha, coluna, flag1=0, flag2=0, flag3=1)
matriz2: float = guardar_dados([[i*0 for i in range(coluna)] for j in range(linha)], linha, coluna, flag1=0, flag2=0, flag3=2)
nova_matriz: float = calcular(matriz1, matriz2, linha, coluna)

for listas in matriz1:
    print(listas)
print("\n")

for listas in matriz2:
    print(listas)
print("\n")
for listas in nova_matriz:
    print(listas)