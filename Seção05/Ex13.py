def guardar_valores() -> int and str:
    """
    :return: valores armazenados
    """
    try:
        a: int = int(input("Digite o valor de A: "))
        b: int = int(input("Digite o valor de B: "))
        simb: str = input("Digite a o simbolo da operação(+ , - , / e *: ")
        if simb not in('+','-','/','*'):
            print('Operação errada!!!')
            return guardar_valores()
        return a, b, simb
    except ValueError as error:
        print("Valor errado!")
        return guardar_valores()


def calcular(a: int, b: int, simb: str) -> int:
    """
    :param a: valor de A
    :param b: valor de B
    :param simb: simbolo da equação
    :return: retorna o resultado da equação
    """
    if simb == '+':
        return a + b
    elif simb == '/':
        return a / b
    elif simb == '-':
        return a - b
    elif simb == '*':
        return a * b


if __name__ == "__main__":
    a, b, simb = guardar_valores()
    print(f'A equação :{a} {simb} {b} tem a resposta: {calcular(a, b, simb)}')
