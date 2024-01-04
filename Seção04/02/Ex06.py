def guardar_valores(x, j, cod) -> int:
    try:
        numero: int = int(input(f"Digite um valor da posição {x} na linha {j}º da Matriz {cod}: "))
        return numero
    except ValueError as error:
        print(f"Valor errado!{error}")
        return guardar_valores(x, j, cod)


def guardar_matrizes(cod) -> int:
    return [[guardar_valores(i, j, cod) for i in range(1, 5)] for j in range(1, 5)]


matriz_A: int = guardar_matrizes(cod=1)
matriz_B: int = guardar_matrizes(cod=2)
matriz_C: int = [[i * 0 for i in range(1, 5)] for j in range(1, 5)]

for i in range(4):
    A: int = matriz_A[i]
    B: int = matriz_B[i]
    C: int = matriz_C[i]
    for j in range(4):
        if A[j] >= B[j]:
            C[j] = A[j]
        elif A[j] < B[j]:
            C[j] = B[j]

print(matriz_A)
print(matriz_B)
print(matriz_C)

