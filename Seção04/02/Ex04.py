def guardar_valores(x, j) -> int:
    try:
        numero: int = int(input(f"Digite um valor da posição {x} na lista {j}º: "))
        return numero
    except ValueError as error:
        print(f"Valor errado!{error}")
        return guardar_valores(x, j)


matriz: int = [[guardar_valores(i, j) for i in range(1, 5)] for j in range(1, 5)]
maior:int = 0
posicao: int = 0
linha: int = 0
for lista in matriz:
    for x in lista:
        if x > maior:
            maior = x
            posicao = lista.index(x)
            linha = matriz.index(lista)
print(f"O maior valor é o {maior} que está linha:{linha+1} e na posição: {posicao+1}!")
