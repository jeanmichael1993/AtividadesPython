def forneca_numero() -> int:
    try:
        numero: int = int(input("Digite um número inteiro entre 100 e 999: "))
        if numero > 999 or numero < 100:
            print(f"O valor {numero} não corresponde ao solicitado")
            forneca_numero()
        return numero
    except ValueError as error:
        print(f"Valor não está de acordo com o solicitado! {error}")
        forneca_numero()


def imprimir_algarismos(x: int):
    valor_em_str: str = str(x)
    print(f"O número usado foi o {x} e seus algarismos são compostos por :{valor_em_str[0]},{valor_em_str[1]},{valor_em_str[2]}")


imprimir_algarismos(forneca_numero())