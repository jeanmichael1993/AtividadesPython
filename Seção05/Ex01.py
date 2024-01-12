
def recebe_numero() -> int:
    """
    Função que recebe valor e devolve o dobro do mesmo.
    :return: o dobro do valor inserido.
    """
    try:
        valor: int = int(input("Digite um numero inteiro: "))
        return valor ** 2
    except ValueError as error:
        print("valor errado!")
    except (TypeError, IndexError) as error:
        print(TypeError, IndexError)


if __name__ == '__main__':
  valor: int = recebe_numero()
  print(valor)
