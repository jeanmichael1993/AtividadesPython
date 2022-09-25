
def valor_aumento(value_product: float):
    taxa: float = 0.0
    if value_product < 50.00:
        taxa = percentual_aumento(1)
    elif value_product >= 50 <= 100:
        taxa = percentual_aumento(2)
    elif value_product > 100:
        taxa = percentual_aumento(3)
    retorno: float = calculo_aumento(taxa, value_product)
    print(retorno)
    mostrar_valor_final(retorno)


def percentual_aumento(cod: int):
    switch={
        1: 0.05,
        2: 0.10,
        3: 0.15
    }
    return switch.get(cod, "Invalid input!")


def calculo_aumento(taxa: float, value_product: float) -> float:
    return (value_product * taxa) + value_product


def mostrar_valor_final(valor_final: float):
    if valor_final < 80:
        print("Barato.")
    elif 80 <= valor_final <= 120:
        print("Normal.")
    elif 120 < valor_final <= 200:
        print("Caro.")
    elif valor_final > 200:
        print("Muito Caro!")


value_product: float = float(input("Digite o valor do produto: "))
valor_aumento(value_product)