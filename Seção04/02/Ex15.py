def dados_gabarito(gabarito: str, count: int) -> int:
    try:
        for x in range(count):
            letra: str = ''
            letra = str(input(f"Digite uma letra da posição {len(gabarito)+1}: "))
            if letra.upper() not in ('A', 'B', 'C', 'D'):
                print("Valor está errado!")
                return dados_gabarito(gabarito, count)
            else:
                gabarito.append(letra)
                count -= 1
        return gabarito
    except ValueError as error:
        print(f"Valor digitado está errado!!!{error}")
        return dados_gabarito(gabarito, count)


def dados_alunos(matriz: str, linha: int, coluna: int, flag1: int, flag2: int) -> int:
    try:
        for i in range(flag1, linha):
            for j in range(flag2, coluna):
                letra: str = ''
                letra = str(input(f"Digite a nota da questão {flag2+1} do aluno{flag1+1}: "))
                if letra.upper() not in ('A', 'B', 'C', 'D'):
                    return dados_alunos(matriz, linha, coluna, flag1, flag2)
                else:
                    matriz[i][j] = letra
                    flag2 += 1
            flag1 += 1
            flag2 = 0
        return matriz
    except ValueError as error:
        print(f"Valor errado!!! {error}")
        return dados_alunos(matriz, linha, coluna, flag1, flag2)


def resultado_notas(resultado: int, gabarito: str, matriz_final: str, linha: int, coluna:int) -> int:

    for i in range(linha):
        count: int = 0
        for j in range(coluna):
            if matriz_final[i][j].upper() == gabarito[j].upper():
                count += 1
        resultado.append(count)
    return resultado


linha: int = 5
coluna: int = 10

matriz: str = [["a" for i in range(coluna)] for j in range(linha)]
gabarito: str = dados_gabarito([], coluna)
matriz_final: str = dados_alunos(matriz, linha, coluna, flag1=0, flag2=0)
resultado: int = resultado_notas([], gabarito, matriz_final, linha, coluna)

print(gabarito)
print(matriz_final)
print(resultado)