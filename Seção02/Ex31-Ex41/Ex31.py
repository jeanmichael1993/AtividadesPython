height: float = float(input("Digite a altura:"))
weight: float = float(input("Digite o peso:"))


def mostrar(x: str):
    print(f"Classificação {x}")


def valida_peso(x: int):
    if weight < 60:
        mostrar(chr(x + 1))
    elif weight >= 60 <= 90:
        mostrar(chr(x + 4))
    elif weight > 90:
        mostrar(chr(x + 7))


valor_letra = 64


if height < 1.20:
    valida_peso(valor_letra)
elif height >= 1.20 <= 1.70:
    valida_peso(valor_letra + 1)
elif height > 1.70:
    valida_peso(valor_letra + 2)

