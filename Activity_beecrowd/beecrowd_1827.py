import sys

def criar_matriz(n):
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    meio = n // 2
    inicio_um = n // 3
    fim_um = n - inicio_um

    # Preencher a diagonal principal com 2
    for i in range(n):
        matriz[i][i] = 2

    # Preencher a diagonal secundária com 3
    for i in range(n):
        matriz[i][n - i - 1] = 3

    # Preencher a parte interna com 1
    for i in range(inicio_um, fim_um):
        for j in range(inicio_um, fim_um):
            matriz[i][j] = 1

    # Preencher o ponto central com 4
    matriz[meio][meio] = 4

    return matriz

def imprimir_matriz(matriz):
    for linha in matriz:
        print("".join(map(str, linha)))

if __name__ == "__main__":
    for linha in sys.stdin:
        try:
            n = int(linha.strip())
            if n % 2 == 1 and 5 <= n <= 101:
                matriz = criar_matriz(n)
                imprimir_matriz(matriz)
                print()
        except EOFError:
            break
