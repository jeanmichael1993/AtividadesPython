def dados_alunos(matriz: float, linha: int, coluna: int, flag1: int, flag2: int) -> float:
    try:
        for i in range(flag1, linha):
            for j in range(flag2, coluna):
                valor: float = 0.0
                valor = float(input(f"Digite a nota da questão {flag2+1} do aluno{flag1+1}: "))
                matriz[i][j] = valor
                flag2 += 1
            flag1 += 1
            flag2 = 0
        return matriz
    except ValueError as error:
        print(f"Valor errado!!! {error}")
        return dados_alunos(matriz, linha, coluna, flag1, flag2)


def resultado_notas(matriz_final: float, linha: int, coluna:int) -> str:

    nota_a: int = 0
    nota_b: int = 0
    nota_c: int = 0
    for i in range(linha):
        piornota: float = 999
        flag: int = -1
        for j in range(coluna):
            if matriz_final[i][j] < piornota:
                piornota = matriz_final[i][j]
                flag = j
            if j == 2:
                if flag == 0:
                    nota_a += 1
                elif flag == 1:
                    nota_b += 1
                elif flag == 2:
                    nota_c += 1
    return print(f"Alunos com a nota pior na prova A: {nota_a}, prova B: {nota_b} e prova C: {nota_c}")


linha: int = 10
coluna: int = 3

matriz: float = [[1*0 for i in range(coluna)] for j in range(linha)]
matriz_final: float = dados_alunos(matriz, linha, coluna, flag1=0, flag2=0)
resultado: float = resultado_notas(matriz_final, linha, coluna)
