def ler_numero() -> int:
    try:
        numero_impar: int = int(input("Digite um numero impar inteiro: "))
        if numero_impar % 2 == 0:
            print("Numero informado não é impar!!!")
            ler_numero()
        return numero_impar
    except ValueError as error:
        print(f"o erro é: {error}, ou seja, o valor consta com erro, por gentileza validar o mesmo.")
        ler_numero()


def imprimir_numeros_impares(n: int):
    try:
        lista_resultado: int = []
        for i in range(n+1):
            if i % 2 != 0:
                lista_resultado.append(i)
        print(lista_resultado)
    except Exception as error:
        print(error)


imprimir_numeros_impares(ler_numero())
