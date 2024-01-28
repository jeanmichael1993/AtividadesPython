import math

def chama_calcular(func):
    """
    :param func: recebe função com dados
    :return: retorno resultado final
    """
    def calcular(*args):
        """
        :param args: valore de x e n
        :return: retorna o valor do número neperiano aproximadamente
        """
        n = func(*args)
        cos_approx = 0
        for i in range(n+1):
            num = 1
            denom = math.factorial(i)
            cos_approx += ((num) / (denom))
        return cos_approx
    return calcular

@chama_calcular
def guardar_valores() -> int and float:
    """
    :return: retorna os valores de x e n
    """
    try:
        n: int = int(input("Digite o valor de N: "))
        return n
    except ValueError as error:
        print('Valor errado!')
        return guardar_valores()


if __name__ == "__main__":
    print(guardar_valores())

