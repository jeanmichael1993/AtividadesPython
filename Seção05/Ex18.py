def soma(numA: int, numB: int) -> int:
    """
    :param numA: valor de A
    :param numB: valor de B
    :return: a exponenciação dos valores
    """
    return numA ** numB


if __name__ == "__main__":
    numA: int = int(input("Digite um numero: "))
    numB: int = int(input("Digite um numero: "))
    print(f'A exponenciação é : {soma(numA, numB)}')