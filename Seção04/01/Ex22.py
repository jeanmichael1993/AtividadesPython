count: int = 4


def popular_vetor(vetor: int, count: int) -> int:
    try:
        for x in range(count):
            vetor.append(int(input(f"Digite o {len(vetor)+1}º número: ")))
            count -= 1
        return vetor
    except ValueError as error:
        print("Valor digitado está errado")
        return popular_vetor(vetor, count)


def criando_vetor_3(vetor_1: int, vetor_2: int):
    vetor_3: int = []
    for i, j in zip(vetor_1, vetor_2):
        vetor_3.append(i)
        vetor_3.append(j)
    print(vetor_3)


vetor_1: int = popular_vetor([], count)
vetor_2: int = popular_vetor([], count)


criando_vetor_3(vetor_1, vetor_2)
