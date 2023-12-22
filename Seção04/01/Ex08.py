valores: int = []
count: int = 6


def imprimir_ao_contrario(count:int):
    try:
        for x in range(count):
            valores.append(int(input(f"Digite um valor da posição {len(valores)+1}ª: ")))
            count -= 1
        print(valores[::-1])
    except ValueError as error:
        print(f"{error}, Um dos valores informados não é um numero inteiro!")
        return imprimir_ao_contrario(count)


imprimir_ao_contrario(count)

