def imprimir(x: int):
    x.sort(reverse=False)
    print(x)


def guardar_numero(x: int) -> int:
    lista_numero = []
    for y in range(x+1):
        lista_numero.append(y)
    return lista_numero



num: int = int(input("Digitar um numero natural inteiro: "))
lista_numero = guardar_numero(num)
imprimir(lista_numero)