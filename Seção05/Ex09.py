import math
def volume_cilindro(raio: float, altura: float) -> float:
    """
    :param raio:
    :param altura:
    :return: volume do cilindro
    """
    v: float = math.pi * (raio**2) * altura
    return v


if __name__ == "__main__":
    raio: float = float(input("Digite o valor do raio: "))
    altura: float = float(input("Digite o valor da altura: "))
    print(f'O valor do volume do cilindro é : {volume_cilindro(raio, altura):.2f}')



