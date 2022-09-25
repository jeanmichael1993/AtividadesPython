km: float = float(input("Distancia em Km: "))
qtd_litro: float = float(input("Quantidade de litros de gasolina consumidos: "))

result: float = km/qtd_litro
if result < 8:
    print("Venda o carro!")
elif result >= 8 and result <= 14:
    print("Econômico!")
elif result > 14:
    print("Super Econômico!")

