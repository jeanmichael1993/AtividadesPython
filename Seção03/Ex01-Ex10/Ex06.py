
numeros: int = []
print("Digite 10 números.")

for x in range(1, 11):
    valor: int = input(f"Digite o número {x}: ")
    numeros.append(int(valor))

print(f"A média dos valores digitados é {sum(numeros)/10:.2f}")
