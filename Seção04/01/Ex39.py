valor: int = int(input("Digite um valor: "))

for n in range(valor):
    print(" " * (valor - n), end="")

    print(" ".join(map(str, str(11 ** n))))

