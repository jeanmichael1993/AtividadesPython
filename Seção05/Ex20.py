def fatorial(func):
    """
    :param func: função de guardar dados
    :return: a funçaõ interna
    """
    def interna(*args):
        """
        :param args: valores recebido da função
        :return: returna o resultado e o numero usado
        """
        resultado: int = func(*args)
        num_soma: int = 1
        for i in range(1, resultado+1):
            num_soma *= i
        return resultado, num_soma
    return interna


@fatorial
def guardar_dados():
    """
    :return: o valor inserido
    """
    try:
        numero: int = int(input("Digite um numero: "))
        return numero
    except ValueError as error:
        print('Valor errado!')
        return guardar_dados()


if __name__ == '__main__':
    numero, resultado = guardar_dados()
    print(f'O fatorial do numero {numero} é : {resultado}')

