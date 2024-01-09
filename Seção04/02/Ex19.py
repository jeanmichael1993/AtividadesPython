def guardar_dados(matriz: int, linha: int, coluna: int, flag1: int, flag2: int) -> int:
    try:
        for i in range(flag1, linha):
            soma: int = 0
            for j in range(flag2, coluna):
                if j == 0:
                    matriz[i][j] = int(input(f"Digite a matricula do aluno({flag1+1}): "))
                elif j == 1:
                    matriz[i][j] = float(input(f"Digite a média da prova do aluno({flag1+1}): "))
                    soma += matriz[i][j]
                elif j == 2:
                    matriz[i][j] = float(input(f"Digite a média dos trabalhos do aluno({flag1+1}):"))
                    soma += matriz[i][j]
                elif j == 3:
                    matriz[i][j] = soma
                flag2 += 1
            flag1 += 1
            flag2 = 0
        return matriz
    except ValueError as error:
        print(f"Valor digitado errado!!!{error}")
        return guardar_dados(matriz, linha, coluna, flag1, flag2)


def maior_nota(matriz: int, linha: int, coluna: int) -> float:
    nota: float = 0
    matricula: int = 0
    for i in range(linha):
        for j in range(coluna):
            if j == 3:
                if matriz[i][j] > nota:
                    nota = matriz[i][j]
                    matricula = matriz[i][0]
    return matricula, nota


def media_aritmetrica(matriz: int, linha: int, coluna: int) -> float:
    media: float = 0
    for i in range(linha):
        for j in range(coluna):
            if j == 3:
                    media += matriz[i][j]
    return media



linha: int = 5
coluna: int = 4
matriz: int = [[i*0 for i in range(coluna)] for j in range(linha)]
matriz_att: int = guardar_dados(matriz, linha, coluna, flag1=0, flag2=0)
vet: int = maior_nota(matriz_att, linha, coluna)
media: float = media_aritmetrica(matriz, linha, coluna)/linha
for listas in matriz_att:
    print(listas)
print(vet)
print(media)

