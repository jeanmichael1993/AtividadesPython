def guardar_valores(vetor: int, count: int) -> int:
    try:
        for x in range(count):
            vetor.append(int(input(f"Digite o {len(vetor)+1}º número: ")))
            count -= 1
        return vetor
    except ValueError as error:
        print(f"Valor digitado está incorreto!! :: {error}")
        return guardar_valores(vetor, count)


def resultado(vetor: int):
    pares: int = [numero for numero in vetor if numero % 2 == 0]
    soma_pares: int = sum(pares)
    impares: int = [numero for numero in vetor if not numero % 2 == 0]
    qtd_impares: int = sum(impares)
    print(pares)
    print(soma_pares)
    print(impares)
    print(qtd_impares)


resultado(guardar_valores([], count=6))

