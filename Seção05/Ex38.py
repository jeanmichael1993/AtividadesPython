import math

def fatorial_exponencial_deco(func):
    def fatorial_exponencial(*n) -> int and float:
        n: int = func(*n)
        fatorial: float = n
        for i in range(1, n):
            fatorial **= (n-i)
        return n, fatorial
    return fatorial_exponencial


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


@fatorial_exponencial_deco
def trata_valor() -> int:
    n = guardar_numero()
    return n



if __name__ == "__main__":
    n, resultado = trata_valor()
    print(f"O fatorial exponencial do número {n} é : {resultado}")

