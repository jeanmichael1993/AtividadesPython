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
    print("####Interseção####")
    print(set(vet1) & set(vet2))


def uniao(vet1: int, vet2: int):
    print("####União####")
    print(set(vet1) | set(vet2))


def diferenca(vet1: int, vet2: int):
    print("####Diferença####")
    print(set(vet1).difference(set(vet2)))


def soma(vet1: int, vet2: int):
    print("####Soma####")
    print([i + j for i, j in zip(vet1, vet2)])


def produto(vet1: int, vet2: int):
    print("####Produto####")
    print([i * j for i, j in zip(vet1, vet2)])


count: int = 5
vet1: int = guardar_valores([], count, cod=1)
vet2: int = guardar_valores([], count, cod=2)
intersecao(vet1, vet2)
diferenca(vet1, vet2)
uniao(vet1, vet2)
soma(vet1, vet2)
produto(vet1, vet2)

