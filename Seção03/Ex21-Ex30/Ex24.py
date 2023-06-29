def ler_numero() -> int:
    try:
        numero: int = int(input("Digite um número inteiro positivo: "))
        if numero <= 0:
            print(f"O número: {numero} é invalido!!!") if numero < 0 else print(f"O número: {numero}, não pode ser 0!!!")
            return ler_numero()
        return numero
    except ValueError as error:
        print(f"Valor invalido!!!{error}")
        return ler_numero()


def soma_divisores(num: int) -> int:
    lista_divisores: int = []
    for i in range(1, num):
        if num % i == 0:
            lista_divisores.append(i)
    soma: int = sum(lista_divisores)
    print(soma)


soma_divisores(ler_numero())
