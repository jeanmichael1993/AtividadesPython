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
    print(f"O maior valor dessa lista é o {max(valores)} e ele se encontra na posição: {valores.index(max(valores))+1}")
    print(f"O menor valor dessa lista é o {min(valores)} e ele se encontra na posição: {valores.index(min(valores))+1}")


mostrar_dados(ler_valores(valores, count))

