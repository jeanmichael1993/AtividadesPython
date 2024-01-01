import math

def guardar_valores(vetor: int = [], count: int = 4) -> int:
    try:
        for x in range(count):
            vetor.append(int(input(f"Dgite o {len(vetor) +1 }º número: ")))
            count -= 1
        return vetor
    except ValueError as error:
        print("Valor digitado está errado!")
        return guardar_valores(vetor, count)


def numero_primo(vetor: int):
    [is_prime(x) for x in vetor]


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i) == 0:
            return False
    return print(n)


numero_primo(guardar_valores())








