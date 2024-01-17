def transformar(celsius: float) -> float:
    """
    :param celsius:
    :return: Fahrenheit
    """
    f: float = celsius * (9.0/5.0) + 32.0
    return f


if __name__ == "__main__":
    celsius: float = float(input("Digite a temperatura em graus Celsius: "))
    print(f'O valor de celsius tranformado em Fahrenheit é :{transformar(celsius):.2f}')

