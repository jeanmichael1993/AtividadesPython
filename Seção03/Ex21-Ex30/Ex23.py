def ler_numero(*args) -> int:
    try:
        numero: int = int(input("Digite um número inteiro positivo: "))
        if numero <= 0:
            print(f"O número: {numero}, está incorreto!") if numero < 0 else print(f"O número: {numero}, não é divisivel!")
            return ler_numero()
        elif numero > 0:
            return numero
    except ValueError as error:
        print(f"O valor está invalido! : {error}")
        return ler_numero()


def imprimir_divisores(x: int):
    lista_divisores: int = []
    for i in range(1, x+1):
        if x % i == 0:
            lista_divisores.append(i)
    print(lista_divisores)


imprimir_divisores(ler_numero())

