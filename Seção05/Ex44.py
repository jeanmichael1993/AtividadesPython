from random import randint


def random(n: int) -> int:
    """
    :param n: quantidade de valores
    :return: retorna lista randomica
    """
    lista: int = []
    valor: int = 0
    while len(lista) < n:
        valor = randint(1, 200)
        if valor not in lista:
            lista.append(valor)
    return lista


def par_impar(vet: int) -> int:
    """
    :param vet: vetor randomico
    :return: pares e impares deste vetor
    """
    a: int = []
    b: int = []
    for i in vet:
        if i % 2 == 0:
            a.append(i)
        else:
            b.append(i)
    a.sort()
    b.sort()
    return a, b


if __name__ == "__main__":
    a, b = par_impar(random(n = 30))
    print(f'O pares são : {a}, e os impares são: {b}')

