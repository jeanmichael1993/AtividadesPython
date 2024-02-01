def inverter_deco(func) -> int:
    """
    :param func: função trata dados
    :return: retorno função decorada
    """
    def inverter(*args) -> int:
        """
        :param args: A e B
        :return: retorna A, B, B e A nessa sequencia
        """
        a, b = func(*args)
        return a, b, b, a
    return inverter


def guardar_dados() -> int:
    """
    :return: retorna valor de A e B
    """
    try:
        a: int = int(input("Digite o valor de A: "))
        b: int = int(input("Digite o valor de B: "))
        return a, b
    except ValueError as error:
        print('Valor está errado!')
        return guardar_dados()


@inverter_deco
def trata_dados() -> int:
    """
    :return: retorna dados tratados
    """
    a, b = guardar_dados()
    return a, b


if __name__ == '__main__':
    a, b, c, d = trata_dados()
    print(f'Valores inseridos {a} e {b} trocados ficam {c} e {d}')