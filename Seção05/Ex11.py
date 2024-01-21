def calcular_media_ari(a: float, b: float , c: float) -> float:
    """
    :param a: valor de A
    :param b: Valor de B
    :param c: Valor de C
    :return: media aritmética
    """
    media: float = (a+b+c) / 3
    return media


def caclular_media_ponderada(a: float, b: float, c: float) -> float:
    """
    :param a: valor de A
    :param b: valor de B
    :param c: valor de C
    :return: media ponderada
    """
    media_p: float = (a * 5 + b * 3 + c * 2) / (5+3+2)
    return media_p


def guardar_dados(notas: float, count: int) -> float:
    """
    :param notas: notas dos alunos
    :param count: quantidade de alunos
    :return: dados dos alunos
    """
    try:
        for i in range(count):
            notas.append(float(input(f'Digite a {len(notas)+1}º nota: ')))
            count -= 1
        return notas
    except ValueError as error:
        print("Valor errado!")
        return guardar_dados(notas, count)


def guardar_letra(a: float, b: float, c: float) -> str:
    """
    :param a: valor de A
    :param b: valor de B
    :param c: valor de C
    :return: media aritmetica ou ponderada
    """
    try:
        letra: str = input('Digite a letra A ou P: ').upper()
        if letra == 'A':
            return print(f'A média aritmética é : {calcular_media_ari(a, b, c):.2f}')
        elif letra == 'P':
            return print(f'A média ponderada é :{caclular_media_ponderada(a, b, c):.2f}')
        else:
            print(f'letra errada! Digite novamente!')
            return guardar_letra()
    except ValueError as error:
        print('Valor errado!')
        return guardar_dados()


if __name__ == "__main__":
    a, b, c = guardar_dados([], count=3)
    guardar_letra(a, b, c)

