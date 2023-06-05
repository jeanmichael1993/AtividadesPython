def ler_numero_impar() -> int:
    try:
        numero_impar: int = int(input("Digite um numero inteiro impar:  "))
        if numero_impar % 2 == 0:
            print("O número digitado não é impar!!!!")
            ler_numero_impar()
        return numero_impar
    except ValueError as error:
        print(f"O sistema gerou o seguinte erro: {error}, ou seja, o valor passado não é um número!")
        ler_numero_impar()


def mostrar_numeros_impares(x: int):
    lista_resultado: int = []
    for i in range(x+1):
        if i % 2 != 0:
            lista_resultado.append(i)
    lista_resultado.reverse()
    print(lista_resultado)


mostrar_numeros_impares(ler_numero_impar())