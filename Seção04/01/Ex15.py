numeros: int = []
count: int = 20


def guardar_numeros(numeros: int, count: int) -> int:
    try:
        numero_guardado: int = 0
        for x in range(count):
            numero_guardado = int(input(f"Digite o {len(numeros)+1}º número: "))
            if numero_guardado not in numeros:
                numeros.append(numero_guardado)
                count -= 1
        print(numeros)
    except ValueError as error:
        print("Valor digitado é incorreto!")
        return guardar_numeros(numeros, count)


guardar_numeros(numeros, count)

