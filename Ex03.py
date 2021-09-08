""" Peça ao usuário para digitar três valores inteiros e imprima a soma deles."""

print("Digite 3 valores inteiros:")
qtd = 3
soma = 0
for num in range(1,3+1):
    soma += (int(input(f"{num}:")))

print(f"{soma}")
