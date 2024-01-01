vetor: int = []
count: int = 100


def guardar_valores(vetor: int, count: int):
    try:
        for x in range(count):
            teste: str = str(x)
            if x == 0:
                continue
            if x % 7 == 0 or teste.endswith("7"):
                print(x)
    except ValueError as error:
        print(error)


guardar_valores(vetor, count)