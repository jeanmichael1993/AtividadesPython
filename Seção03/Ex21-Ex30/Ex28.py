def ler_numero() -> int:
    try:
        numero: int = int(input("Digite um número inteiro positivo: "))
        if numero <= 0:
            print(f"Numero não pode ser negativo! número digitado:{numero}") if numero < 0 else print("Número não pode ser 0!!!")
            return ler_numero()
        return numero
    except ValueError as error:
        print(f"Valor não aceito!!!{error}")
        return ler_numero()


def calcular_valor_e(x: int) -> float:
    e: float = 1
    for i in range(1, x+1):
        resultado: float = 1
        for j in range(1, i+1):
            resultado *= j
        e += 1/resultado
    return e


def mostrar_valor_e(e: float):
    print(f'O valor é do número escolhido é: {e}')


mostrar_valor_e(calcular_valor_e(ler_numero()))