
matriz: int = [[i * 0 for i in range(1, 11)] for j in range(1, 11)]

for i in range(10):
    mat: int = matriz[i]
    for j in range(10):
        if i < j:
            mat[j] = (2*i) + (7*j) - 2
        elif i == j:
            mat[j] = (3 * i)**2 - 1
        else:
            mat[j] = (4*i)**3 - (5*j)**2 + 1

print(matriz)
