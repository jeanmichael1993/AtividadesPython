numeros: int = []
count: int = 4


def ler_valores(numeros: int, count: int) -> int:
    try:
        for x in range(count):
            numeros.append(int(input(f"Digite o {len(numeros)+1}º número: ")))
            count -= 1
        return numeros
    except ValueError as error:
        print("Valor digitado está incorreto!")
        return ler_valores(numeros, count)


def valores_iguais(numeros: int) -> str:
    numeros_iguais: int = []
    numeros.sort()
    for x in range(len(numeros)):
            if numeros[x-1] == numeros[x]:
                if x not in numeros_iguais:
                    numeros_iguais.append(numeros[x])
                else:
                    pass
    return numeros_iguais


def mostrar_resposta(lista: str):
    if len(lista) > 0:
        print(lista)
    else:
        print("Não possui números repetidos na lista!")


mostrar_resposta(valores_iguais(ler_valores(numeros, count)))
