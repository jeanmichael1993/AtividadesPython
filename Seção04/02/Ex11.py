matriz: int = [[1*0 for i in range(1, 4)] for j in range(1, 4)]
soma: int = 1

"""
guardar dados 1 a 9 na matriz
"""
for i in range(3):
    for j in range(3):
        matriz[i][j] = soma
        soma += 1
"""
somar numeros da diagonal secundaria
"""
soma_2: int = 0
for i in range(3):
    for j in range(3):
        if i+j == 2:
            soma_2 += (matriz[i][j])
print(soma_2)
