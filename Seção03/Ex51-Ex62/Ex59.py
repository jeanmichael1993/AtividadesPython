def calcular_consumo_total(cidade):
    consumo_residencial = 0
    consumo_comercial = 0
    consumo_industrial = 0

    maior_consumo = float('-inf')
    menor_consumo = float('inf')
    soma_consumo = 0
    total_habitantes = len(cidade)

    for habitante in cidade:
        consumo, codigo = habitante

        if consumo > maior_consumo:
            maior_consumo = consumo

        if consumo < menor_consumo:
            menor_consumo = consumo

        soma_consumo += consumo

        if codigo == 1:
            consumo_residencial += consumo
        elif codigo == 2:
            consumo_comercial += consumo
        elif codigo == 3:
            consumo_industrial += consumo

    media_consumo = soma_consumo / total_habitantes

    print("Maior consumo:", maior_consumo)
    print("Menor consumo:", menor_consumo)
    print("Média de consumo:", media_consumo)
    print("Total de consumo residencial:", consumo_residencial)
    print("Total de consumo comercial:", consumo_comercial)
    print("Total de consumo industrial:", consumo_industrial)


def ler_dados_habitantes():
    cidade = []
    num_habitantes = int(input("Digite o número de habitantes da cidade: "))
    valor_kwh = float(input("Digite o valor do kWh: "))

    for i in range(1, num_habitantes + 1):
        consumo = float(input(f"Digite o consumo do habitante {i}: "))
        codigo = int(input(f"Digite o código do consumidor do habitante {i} (1-Residencial, 2-Comercial, 3-Industrial): "))
        cidade.append((consumo, codigo))

    return cidade


# Função principal
def main():
    cidade = ler_dados_habitantes()
    calcular_consumo_total(cidade)


if __name__ == "__main__":
    main()
