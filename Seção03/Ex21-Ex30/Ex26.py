def encontrar_multiplo(num: int) -> int:
    i = num + 1
    while True:
        if i % 11 == 0 or i % 13 == 0 or i % 17 == 0:
            return i
        i += 1


def numero_obtido() -> int:
    try:
        numero: int = int(input("Digite um número inteiro positivo: "))
        if numero <= 0:
            print(f'{numero} é invalido!!!') if numero < 0 else print(f'O número: {numero},não pode ser 0!!! ')
            return numero_obtido()
        return numero
    except ValueError as error:
        print(f"Valor invalido!!!{error}")
        return numero_obtido()


print(f"O primeiro múltiplo de 11, 13 ou 17 é", encontrar_multiplo(numero_obtido()))
