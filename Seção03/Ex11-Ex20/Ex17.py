def ler_numero() -> int:
    try:
        n: int = int(input("Digite um numero inteiro positivo: "))
        if n < 0:
            print("O número informado deve ser maior ou igual a 0!!!")
            ler_numero()
        return n
    except ValueError as error:
        print(f"O valor inserido não é um valor aceito!!! segue erro: {error}")
        ler_numero()


def calcular_soma(x: int):
    soma: int = 0
    for i in range(x+1):
        soma += i
    print(f"A soma dos {x} primeiros números naturais é : {soma}")


calcular_soma(ler_numero())

