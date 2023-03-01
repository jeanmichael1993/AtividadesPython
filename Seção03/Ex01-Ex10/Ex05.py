
numeros: int = []
print("Digite 10 números.")
for x in range(1, 11):
    numeros.append(input(f"Digite o número {x}: "))

soma: int = 0
for x in numeros:
    soma = soma + int(x)


print(f"a somatoria é {soma}")
