def soma(numA: int, numB: int) -> int:
    """
    :param numA: valor de A
    :param numB: valor de B
    :return:  soma dos numeros entre eles
    """
    soma: int = 0
    if numA >= numB:
        for i in range(numB, numA+1):
            soma += i
    else:
        for i in range(numA, numB+1):
            soma += i
    return soma


if __name__ == "__main__":
    numA: int = int(input("Digite um numero: "))
    numB: int = int(input("Digite um numero: "))
    print(f'A soma dos numeros entre os descritos é: {soma(numA, numB)}')