vetor: int = []
count: int = 10


def guardar_valor(vetor: int, count: int) -> int:
    try:
        numero: int = None
        for x in range(count):
            numero = int(input(f'Digite o {len(vetor)+1}º numero: '))
            count -= 1
            if numero < 0:
                vetor.append(0)
            else:
                vetor.append(numero)
        return vetor
    except ValueError as error:
        print("Valor inserido está errado!")
        return guardar_valor(vetor, count)


def mostrar_vetor(vetor: int):
    print(vetor)


mostrar_vetor(guardar_valor(vetor, count))