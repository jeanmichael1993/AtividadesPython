matriz: int = [[1*0 for i in range(1, 4)] for j in range(1, 4)]
matriz_2: int = [[1*0 for i in range(1, 4)] for j in range(1, 4)]
soma: int = 1

"""
guardar dados 1 a 9 na matriz
"""
for i in range(3):
    for j in range(3):
        matriz[i][j] = soma
        soma += 1
"""
transposta da matriz 
"""

for i in range(3):
    for j in range(3):
        matriz_2[j][i] = matriz[i][j]
print(matriz)
print(matriz_2)
