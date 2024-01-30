def fatorial_deco(func) -> int and str:
    def fatorial(*args) -> int and str:
        n = func(*args)
        multi: int = 1
        soma: int = 0
        lista: str = []
        for i in range(1, n+1):
            multi *= i
        for i in str(multi):
            lista.append(i)
            soma += int(i)
        return lista, soma
    return fatorial

@fatorial_deco
def guardar_dados() -> int:
    try:
        n: int = int(input("Digite o valor de N: "))
        return n
    except ValueError as erro:
        print("Valor errado!")
        return guardar_dados()


if __name__  == "__main__":
    lista, soma = guardar_dados()
    print(f'{"+".join(lista)} = {soma}')