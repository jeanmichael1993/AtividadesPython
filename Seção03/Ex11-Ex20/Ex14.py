def imprimir(x: int):
    x.sort(reverse = True)
    print(x)


def guardar_numero(x: int) -> int:
    lista_num: int = []
    for y in range(x+1):
        if y % 2 == 0:
            lista_num.append(y)
    return lista_num



num: int = int(input("Digite um número par: "))
lista_num = guardar_numero(num)
imprimir(lista_num)