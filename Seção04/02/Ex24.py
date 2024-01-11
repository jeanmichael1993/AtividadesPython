def obter_matriz():
    matriz = []
    print("Digite os elementos da matriz 20x20:")
    for _ in range(20):
        linha = [int(num) for num in input().split()]
        matriz.append(linha)
    return matriz

def maior_produto(matriz):
    maior = 0

    # Verifica horizontalmente
    for i in range(20):
        for j in range(17):
            produto = matriz[i][j] * matriz[i][j+1] * matriz[i][j+2] * matriz[i][j+3]
            maior = max(maior, produto)

    # Verifica verticalmente
    for i in range(17):
        for j in range(20):
            produto = matriz[i][j] * matriz[i+1][j] * matriz[i+2][j] * matriz[i+3][j]
            maior = max(maior, produto)

    # Verifica diagonalmente (\)
    for i in range(17):
        for j in range(17):
            produto = matriz[i][j] * matriz[i+1][j+1] * matriz[i+2][j+2] * matriz[i+3][j+3]
            maior = max(maior, produto)

    # Verifica diagonalmente (/)
    for i in range(17):
        for j in range(3, 20):
            produto = matriz[i][j] * matriz[i+1][j-1] * matriz[i+2][j-2] * matriz[i+3][j-3]
            maior = max(maior, produto)

    return maior

# Obtém a matriz do usuário
matriz_usuario = obter_matriz()

# Calcula e exibe o maior produto
resultado = maior_produto(matriz_usuario)
print(f"O maior produto de quatro números adjacentes é: {resultado}")
