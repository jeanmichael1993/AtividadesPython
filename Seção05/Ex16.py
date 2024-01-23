def printar(qtd: int):
    """
    :param qtd: quantidade de '='
    :return: mostra em linha
    """
    mostrar: str = ''
    for i in range(qtd):
        mostrar += '='
    print(mostrar)

if __name__ == '__main__':
    qtd: int = int(input('Digite um valor inteiro: '))
    printar(qtd)
