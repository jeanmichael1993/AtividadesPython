import math

def chama_calcular(func):
    """
    :param func: recebe função com dados
    :return: retorno resultado final
    """
    def calcular(*args):
        """
        :param args: valore de x e n
        :return: retorna o valor do cosseno hiperbólico aproximadamente
        """
        x, n = func(*args)
        cos_approx = 0
        for i in range(n+1):
            num = x**(2*i)
            denom = math.factorial(2 * i)
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
        x: float = float(input("Digite o valor para o radianos: "))
        return math.radians(x), n
    except ValueError as error:
        print('Valor errado!')
        return guardar_valores()


if __name__ == "__main__":
    print(guardar_valores())

