
def maior_fator_primo(func):
    """
    :param func: funcão decorada
    :return: retorna o maior fator primo
    """
    def interna(*args, **kwargs):
        """
        :param args: paramentros
        :param kwargs: paramentros
        :return: retorna o maior fator primo
        """
        #Busca a funcão guardar numero
        numero = func(*args, **kwargs)
        # Inicializa o maior fator primo como 1
        maior_fator = 1

        # Divide o número por 2 até que não seja mais divisível por 2
        while numero % 2 == 0:
            maior_fator = 2
            numero = numero // 2

        # Divide o número por ímpares a partir de 3
        for i in range(3, int(numero ** 0.5) + 1, 2):
            while numero % i == 0:
                maior_fator = i
                numero = numero // i

        # Se o número restante for maior que 2, esse é o maior fator primo
        if numero > 2:
            maior_fator = numero

        return maior_fator
    return interna


#primeiro vair chamar o maior fator primo e depois vai chamar essa função dentro de outra função
@maior_fator_primo
def guardar_numero() -> int:
    """
    :return: o numero inserido
    """
    try:
        numero: int = int(input("Digite um número: "))
        return numero
    except ValueError as erro:
        print("Valor Errado!")
        return guardar_numero()


if __name__ == "__main__":
    resultado:int = int(guardar_numero())
    print(f"O maior fator primo é {resultado}")
