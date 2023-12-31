count: int = 5


def produzir_vetores(vetor: int, count: int) -> int:
    try:
        for x in range(count):
            vetor.append(int(input(f"Digite o {len(vetor)+1}º número: ")))
            count -= 1
        return vetor
    except ValueError as error:
        print("Valor digitado está errado!")
        return produzir_vetores(vetor, count)


def produto_escalar(vetor_1: int,vetor_2: int) -> int:
    soma: int = 0
    for x, y in zip(vetor_1, vetor_2):
        soma += x * y
    print(vetor_1)
    print(vetor_2)
    print(soma)


vetor_1: int = produzir_vetores([], count)
vetor_2: int = produzir_vetores([], count)
produto_escalar(vetor_1, vetor_2)

