def soma_matrizes(matriz1, matriz2):
    resultado = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            resultado[i][j] = matriz1[i][j] + matriz2[i][j]
    return resultado

def subtrai_matrizes(matriz1, matriz2):
    resultado = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            resultado[i][j] = matriz1[i][j] - matriz2[i][j]
    return resultado

def adiciona_constante(matriz, constante):
    for i in range(2):
        for j in range(2):
            matriz[i][j] += constante
    return matriz

def imprime_matrizes(matriz1, matriz2):
    print("Matriz 1:")
    for row in matriz1:
        print(row)
    print("Matriz 2:")
    for row in matriz2:
        print(row)

# Leitura das matrizes
matriz1 = []
matriz2 = []
for i in range(2):
    row1 = [float(input(f"Digite o valor para a matriz 1 na posição ({i + 1}, 1): ")),
            float(input(f"Digite o valor para a matriz 1 na posição ({i + 1}, 2): "))]
    matriz1.append(row1)

for i in range(2):
    row2 = [float(input(f"Digite o valor para a matriz 2 na posição ({i + 1}, 1): ")),
            float(input(f"Digite o valor para a matriz 2 na posição ({i + 1}, 2): "))]
    matriz2.append(row2)

# Menu de opções
while True:
    print("\nMenu:")
    print("(a) Somar as duas matrizes")
    print("(b) Subtrair a primeira matriz da segunda")
    print("(c) Adicionar uma constante às duas matrizes")
    print("(d) Imprimir as matrizes")
    print("(e) Sair")

    escolha = input("Escolha uma opção (a/b/c/d/e): ")

    if escolha == 'a':
        resultado_soma = soma_matrizes(matriz1, matriz2)
        print("Resultado da soma das matrizes:")
        for row in resultado_soma:
            print(row)
    elif escolha == 'b':
        resultado_subtracao = subtrai_matrizes(matriz1, matriz2)
        print("Resultado da subtração das matrizes:")
        for row in resultado_subtracao:
            print(row)
    elif escolha == 'c':
        constante = float(input("Digite a constante a ser adicionada às matrizes: "))
        matriz1 = adiciona_constante(matriz1, constante)
        matriz2 = adiciona_constante(matriz2, constante)
        print("Matrizes após adição da constante:")
        imprime_matrizes(matriz1, matriz2)
    elif escolha == 'd':
        imprime_matrizes(matriz1, matriz2)
    elif escolha == 'e':
        break
    else:
        print("Opção inválida. Tente novamente.")