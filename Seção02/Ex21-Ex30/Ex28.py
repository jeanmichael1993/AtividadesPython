valor_um: int = int(input("Digite o primeiro número: "))
valor_dois: int = int(input("Digite o segundo número: "))
valor_tres: int = int(input("Digite o terceiro número: "))

ponderada: float = (valor_um + 2 * valor_dois + 3 * valor_tres) / 6

print(f"A media ponderada é: {ponderada}")