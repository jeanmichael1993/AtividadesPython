import math
def hipotenusa(a: float, b: float) -> float:
    """
    :param a: valor de A
    :param b: Valor de B
    :return: Hipotenusa
    """
    h: float = math.sqrt((a**2)+(b**2))
    return h


if __name__ == "__main__":
    a: float = float(input("Digite o valor de A: "))
    b: float = float(input("Digite o valor de B: "))
    print(f'O valor da hipotenusa é {hipotenusa(a, b):.2f}')



