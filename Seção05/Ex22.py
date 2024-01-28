def gerar(func):
    """
    :param func: função guarda valor
    :return: função interna
    """
    def interna(*args):
        """
        :param args: argumentos
        :return: retorna nada
        """
        n: int = func(*args)
        concat: str = ''
        for i in range(n):
            concat += '!'
            print(concat)
        return None
    return interna


@gerar
def guarda_valor() -> int:
    """
    :return: returna valor inserido
    """
    try:
        num: int = int(input("Digite um numero: "))
        return num
    except ValueError as error:
        print("Valor errado!")
        return guarda_valor()


if __name__ == '__main__':
    guarda_valor()

