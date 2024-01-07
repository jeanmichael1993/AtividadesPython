import random

def guardar_numero(cartela: int) -> int:
    numeros: int = [i for i in range(100)]
    for i in range(5):
        for j in range(5):
            if cartela[i][j] == -1:
                        numero_random: int = random.choice(numeros)
                        cartela[i][j] = numero_random
                        numeros.remove(numero_random)
    return cartela


cartela: int = [[1*-1 for i in range(5)] for j in range(5)]
cartela_bingo: int = guardar_numero(cartela)

for lista in cartela_bingo:
    print(lista)