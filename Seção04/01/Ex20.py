vetor: int = []
count: int = 10
segundo_vetor: int = []


def ler_valores(vetor: int, count: int) -> int:
    try:
        valor: int = None
        for x in range(count):
            valor = int(input(f"Digite o {len(vetor)+1} número entre 0 e 50: "))
            if 0 <= valor <= 50:
                vetor.append(valor)
                count -= 1
            else:
                print("Valor inserido está errado!")
                return ler_valores(vetor, count)
        return vetor
    except ValueError as error:
        print("Valor digitador está incorreto!")
        return ler_valores(vetor, count)


def preencher_segundo_vetor(vetor: int, segundo_vetor: int) -> int:
    for x in vetor:
        if x % 2 != 0:
            segundo_vetor.append(x)


ler_valores(vetor, count)
segundo_vetor = filter(lambda x: x % 2 != 0, vetor)
print(list(segundo_vetor))
print(vetor)

