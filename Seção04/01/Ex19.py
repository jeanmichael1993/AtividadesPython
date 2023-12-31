vetor: int = []
count: int = 50


def calculo(numero: int) -> str:
    return print(f'{numero} + 5 * {numero}) % ({numero} + 1)\n')


[calculo(x) for x in range(1, count+1)]
