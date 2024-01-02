from collections import Counter


def guardar_dados(vetor: int, count: int):
    try:
        for x in range(count):
            valor: int = int(input(f"Digite o {len(vetor) + 1}º número: "))
            # valida em um dicionario quantos valores tem.
            if valor in Counter(vetor):
                print(f"O valor {valor} já foi digitado antes, inserir novamente!")
                return guardar_dados(vetor, count)
            else:
                vetor.append(valor)
                count -= 1
        return vetor
    except ValueError as error:
        print(f"Valor digitado está errado!!! {error}")
        return guardar_dados(vetor, count)


print(guardar_dados([], count=10))