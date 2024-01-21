def guardar_dados() -> str:
    """
    :return: dados salvos
    """
    try:
        numero: str = input("Digite um número maior que 0: ")
        if int(numero) <= 0:
            return "valor erraado!"
        else:
            return numero
    except ValueError as error:
        print(f'Valor errado!')
        return guardar_dados()


def somar(numero: str) -> int:
    """
    :param numero: valor inserido
    :return: retorna soma do numero
    """
    soma: int = 0
    for i in numero:
        soma += int(i)
    return soma


if __name__ == '__main__':
    print(f'A soma do numero é : {somar(guardar_dados())}')