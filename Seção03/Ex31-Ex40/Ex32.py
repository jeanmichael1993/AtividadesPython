from random import randint


def numero_de_vezes() -> int:
    try:
        numero: int = int(input("Digite um número inteiro positivo: "))
        if numero <= 0:
            print(f'O valor fornecido está incorreto: {numero}')
            return numero_de_vezes()
        return numero
    except ValueError as error:
        print(f'Valor incorreto!{error}')
        return numero_de_vezes()


def dados_random(n: int) -> int:
    dado1: int = []
    dado2: int = []
    for i in range(n):
        dado1.append(randint(1, 6))
        dado2.append(randint(1, 6))
    return dado1, dado2


def mostrar_resultado(dados: int):
    for t in range(len(dados[0])):
        if dados[0][t] == dados[1][t]:
            print(f'{dados[0][t]} = {dados[1][t]}')
        elif dados[0][t] > dados[1][t]:
            print(f'{dados[0][t]} > {dados[1][t]}')
        elif dados[0][t] < dados[1][t]:
            print(f'{dados[0][t]} < {dados[1][t]}')


mostrar_resultado(dados_random(numero_de_vezes()))