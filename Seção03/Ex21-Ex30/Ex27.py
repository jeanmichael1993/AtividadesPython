def inserir_numero() -> int:
    try:
        numero: int = int(input("Digite um número inteiro positivo: "))
        if numero <= 0:
            print(f"{numero} é negativo, pontato incorreto!") if numero < 0 else print(f'0 número digitado:{numero},não pode ser 0!!')
            return inserir_numero()
        return numero
    except ValueError as error:
        print(f'Valor não aceito!{error}')
        return inserir_numero()


def numero_harmonico(x: int) -> float:
    soma: float = 1
    for i in range(2, x+1):
        soma += 1/i
    return soma


def mostrar_soma(soma: float):
    print(f'O valor da soma harmônica deste número é : {soma:.2f}')


mostrar_soma(numero_harmonico(inserir_numero()))