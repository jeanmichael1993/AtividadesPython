import statistics


valores: int = []
count: int = 5


def ler_valores(valores: int, count: int) -> int:
    try:
        for x in range(count):
            valores.append(int(input(f"Digite o {len(valores) + 1}º número: ")))
            count -= 1
        return valores
    except ValueError as error:
        print("Valor digitado está errado!")
        return ler_valores(valores, count)


def mostrar_dados(valores: int):
    print(f"Os valores inseridos foram: {valores}")
    print(f"O maior valor dessa lista é o {max(valores)}")
    print(f"O menor valor dessa lista é o {min(valores)}")
    print(f"A media dos valores é {statistics.mean(valores)}")


mostrar_dados(ler_valores(valores, count))

