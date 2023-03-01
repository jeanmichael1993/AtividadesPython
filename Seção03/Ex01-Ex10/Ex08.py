numeros: int = []
print("Digite 10 números.")
for x in range(1, 11):
    numeros.append(int(input(f"Digite o número {x}: ")))

print(f"O maior valor é o {max(numeros)} e o menor número é o {min(numeros)}")