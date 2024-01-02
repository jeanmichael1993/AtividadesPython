def guardar_valores(vetor: int, count: int, cod: int) -> int:
    try:
        for x in range(count):
            vetor.append(int(input(f"Digite o {len(vetor)+1}º número do vetor ({cod}): ")))
            count -= 1
        return vetor
    except ValueError as error:
        print(f'Valor digitado está errado!!! {error}')
        return guardar_valores(vetor, count, cod)


def intersecao(vet1: int, vet2: int):
    print(set(vet1) & set(vet2))


intersecao(guardar_valores([], count=10, cod=1), guardar_valores([], count=10, cod=2))

