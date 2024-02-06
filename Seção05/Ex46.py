
def guardar_valor(n: int, count: int, lista_vet: float) -> float:
    try:
        for i in range(count, n):
            lista_vet.append(float(input(f"Digite o número da {len(lista_vet)+1}ª posição:  ")))
            count += 1
        return lista_vet
    except ValueError as error:
        print("Valor errado!")
        return guardar_valor(n, count, lista_vet)


def imprimir(vet: float):
    print(vet)


def imprimir_contrario(vet: float):
    lista_contra: float = vet[::-1]
    print(lista_contra)


def media_arit(vet: float):
    soma: float = 0.0
    for i in vet:
        soma += i
    print(f'A média é: {soma/len(vet)}')


if __name__ == "__main__":
    try:
        n: int = int(input("Digite um valor para a quantidade de números no vetor: "))
        vet: float = guardar_valor(n, count=0, lista_vet = [])
        imprimir(vet)
        imprimir_contrario(vet)
        media_arit(vet)
    except ValueError as error:
        print('valor está errado!')
