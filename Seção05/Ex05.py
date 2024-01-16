import math
def calcuar_volume_esfera(raio: float) -> float:
    """
    Função para calcular o volume de uma esfera
    :param raio:
    :return:
    """
    return (4/3) * math.pi * (raio**3)


if __name__ == "__main__":
    raio: float = float(input("Digite o raio: "))
    print(f'{calcuar_volume_esfera(raio):.2f}')

