

def calcular_comissao(value_sale: float) -> float:
    if value_sale >= 100000:
        return (value_sale * 0.16) + 700
    elif 100000 > value_sale >= 80000:
        return (value_sale * 0.14) + 650
    elif 80000 > value_sale >= 60000:
        return (value_sale * 0.14) + 600
    elif 60000 > value_sale >= 40000:
        return (value_sale * 0.14) + 550
    elif 40000 > value_sale >= 20000:
        return (value_sale * 0.14) + 500
    elif value_sale < 20000:
        return (value_sale * 0.14) + 400


def mostrar_comissao(result: float):
    print(f"O valor da comissão é de: {result:.2f}")








value_sale: float = float(input("Digite o valor da venda: "))
comissao: float = calcular_comissao(value_sale)
mostrar_comissao(comissao)

