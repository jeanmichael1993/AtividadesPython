import math


def fatorial_quadruplo_deco(func):
    def fatorial_guadruplo(*args):
        n = func(*args)
        return n, (math.factorial(2*n)) / math.factorial(n)
    return fatorial_guadruplo


@fatorial_quadruplo_deco
def guardar_numero():
    try:
        n: int = int(input("Digite o numero: "))
        return n
    except ValueError as error:
        print("valor errado!")
        return guardar_numero()


if __name__ == "__main__":
    n, resultado = guardar_numero()
    print(f"O fatorial quádruplo do número {n} é : {resultado}")

