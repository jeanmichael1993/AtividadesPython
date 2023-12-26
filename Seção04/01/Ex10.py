notas: float = []
count: int = 15


def adicionar_notas(count: int):
    try:
        for x in range(count):
            notas.append(float(input(f"Digite o nota do {len(notas)+1}º aluno: ")))
            count -= 1
        print(f"{calcular_media(notas):.2f}")
    except ValueError as error:
        print("Valor incorreto!")
        return adicionar_notas(count)


def calcular_media(notas: float) -> float:
    soma: float = 0
    for i in (notas):
        soma += i
    return soma/15


adicionar_notas(count)