import math


def superfatorial_deco(func):
    def superfatorial(*n):
        n: int = (func(*n))
        soma: int = 1
        for i in range(1, n+1):
            soma *= math.factorial(i)
        return n, soma
    return superfatorial


def guardar_numero():
    try:
        n: int = int(input("Digite o numero: "))
        while n <= 0:
            print('Valor não pode ser menor que 1!')
            n: int = int(input("Digite o numero: "))
        return n
    except ValueError as error:
        print("valor errado!")
        return guardar_numero()

@superfatorial_deco
def trata_valor() -> int:
    n = guardar_numero()
    return n



if __name__ == "__main__":
    n, resultado = trata_valor()
    print(f"O superfatorail  do número {n} é : {resultado}")

