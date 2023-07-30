def ler_numeros() -> int:
    vetor: int = []
    for x in range(8):
        try:
            vetor.append(int(input(f"Digite o valor da posição {x+1} para o vetor: ")))
        except ValueError as error:
            print(error)
            return ler_numeros()
    return vetor

def ler_x_y(i: int) -> int:
    try:
        x: int = int(input("Digite um valor para X: "))
        if x <= 0 and x >= 9:
            print("Valor de X invalido, precisa ser entre 1 e 8!")
            return ler_x_y()
        y: int = int(input("Digite um valor para Y: "))
        if y <= 0 and x >= 9:
            print("Valor de Y invalido, preicsa ser entre 1 e 8!")
            return ler_x_y()
        return i[x-1], i[y-1]
    except ValueError as error:
        print(f"Valor invalido, {error}")
        return ler_x_y()


x, y = ler_x_y(ler_numeros())
print(x + y)