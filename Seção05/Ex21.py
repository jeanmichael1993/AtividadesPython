import math


def valida_prime(valor: int) -> int:
    """
    :param valor: numero para validar
    :return: validação se é primo ou não
    """
    for i in range(2, int(math.sqrt(valor)) + 1):
        if (valor % i) == 0:
            return False
    return True


def is_prime(func):
    """
    :param func: receba a função de guardar valor
    :return: retorna o resultado
    """
    def interna(*args):
        """
        :param args: valores
        :return: a lista de numeros primos abaixo do número citado
        """
        n = func(*args)
        lista: int = []
        for j in range(2, n+1):
            res: bool = valida_prime(j)
            if res:
                lista.append(j)
        return lista
    return interna


@is_prime
def guardar_valor():
    """
    :return: guarda o numero que vai ser utilizado como ponto de parada.
    """
    try:
        numero: int = int(input("Digite um numero: "))
        return numero
    except ValueError as error:
        print('Valor errado!')
        return guardar_valor()


if __name__ == "__main__":
    print(guardar_valor())


