def calculo_custo_total(custo_fabrica:float) -> float:
    if custo_fabrica <= 12_000:
        return (custo_fabrica * 0.05) + custo_fabrica
    elif custo_fabrica > 12_000 and custo_fabrica <= 25_000:
        return  ((custo_fabrica * 0.10) + custo_fabrica) + ((custo_fabrica * 0.15) + custo_fabrica)
    elif custo_fabrica > 25_000:
        return ((custo_fabrica * 0.15) + custo_fabrica) + ((custo_fabrica * 0.20) + custo_fabrica)


def mostrar_custo(custo_final: float):
    print(f'R${custo_final:.2f}.')


custo_fabrica:float = float(input("Digite o custo de Fábrica: "))
mostrar_custo(calculo_custo_total(custo_fabrica))
