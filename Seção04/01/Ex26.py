import statistics

vetor: float = []
count: int = 10


def guardar_dados(vetor: float, count: int) -> float:
    try:
        for x in range(count):
            vetor.append(float(input(f"Digite o {len(vetor)+1}º número: ")))
            count -= 1
        return vetor
    except ValueError as error:
        print('Valor digitado está errado!')
        return guardar_dados(vetor, count)


def desvio_padrao(vetor: float, count):
    media: float = statistics.mean(vetor)
    soma: float = 0
    for x in vetor:
        soma += (x-media)**2
    print(f"O desvio padrão é de : {(soma/ count):.3f}")


desvio_padrao(guardar_dados(vetor, count), count)

