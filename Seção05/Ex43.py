from random import randint


def random(n: int) -> int:
    lista: int = []
    valor: int = 0
    while len(lista) < n:
        valor = randint(1, 200)
        if valor not in lista:
            lista.append(valor)
    return lista


if __name__ == "__main__":
    n: int = int(input("Digite o valor de N: "))
    print(random(n))
