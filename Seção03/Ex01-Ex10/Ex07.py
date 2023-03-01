
positivos: int = []


def criar_lista(cont: int):
    while len(positivos) < 10:
        x: int = int(input(f"Digite o número {cont}: "))
        if x < 0:
            criar_lista(cont)
        else:
            positivos.append(x)
            cont += 1


criar_lista(1)
print(f"A média é {sum(positivos)/10:.2f}")