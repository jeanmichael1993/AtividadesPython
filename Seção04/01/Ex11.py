numeros: int = []
count: int = 10


def guardar_numeros(count: int, numeros: int) -> int:
    try:
        for i in range(count):
            numeros.append(int(input(f"Digite o {len(numeros)+1}º número: ")))
            count -= 1
        return numeros
    except ValueError as error:
        print("Valor digitado está errado! ")
        return guardar_numeros(count, numeros)


def negativos_e_positivos(valores: int) -> int:
    soma: int = 0
    quantidade: int = 0
    for x in (valores):
        if x < 0:
            quantidade += 1
        elif x > 0:
            soma += x
        else:
            continue
    return soma, quantidade


def mostrar_resultado(soma: int, quantidade: int):
    print(f"A soma dos números positivos é: {soma}, e a quantidade de números negativos é de {quantidade}!")


soma, quantidade = negativos_e_positivos(guardar_numeros(count, numeros))
mostrar_resultado(soma, quantidade)

