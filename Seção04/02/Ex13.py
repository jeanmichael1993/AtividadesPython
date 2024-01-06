matriz: int = [[1*0 for i in range(1, 5)] for j in range(1, 5)]
soma: int = 1

"""
guardar dados 1 a 9 na matriz
"""
for i in range(4):
    for j in range(4):
        matriz[i][j] = soma
        soma += 1

for lista in matriz:
    print(lista)

print('\n')
"""
Transformação da matriz em triangular inferior
"""

for i in range(4):
    for j in range(4):
        if i < j:
            matriz[i][j] = 0


for lista in matriz:
    print(lista)
