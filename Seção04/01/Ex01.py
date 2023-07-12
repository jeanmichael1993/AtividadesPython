vetor_a: int = [1, 0, 5, -2, -5, 7]
lista_soma: int = [vetor_a[0], vetor_a[1], vetor_a[5]]
soma: int = sum(lista_soma)
print(f"A soma é : {soma}")
vetor_a[4] = 100
for i in vetor_a:
    print(i)