def converter_segundos(horas: int, minutos: int, segundos: int) -> int:
    """
    Converte os valores em segundos
    :param horas:
    :param minutos:
    :param segundos:
    :return: segundos
    """
    segundos_totais: int = 0
    segundos_totais = ((horas*60)*60) + (minutos*60) + segundos
    return segundos_totais


if __name__ == '__main__':
    horas: int = int(input("Digite o valor das horas:  "))
    minutos: int = int(input("Digite os minutos: "))
    segundos: int = int(input("Digite os segundos: "))
    res: int = converter_segundos(horas, minutos, segundos)
    print(f'segundos totais: {res}')

