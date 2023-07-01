def intervalo() -> int:
    try:
        intervalo_incial: int = int(input("Digite um valor para difinir o intervalo(positivo e inteiro) Inicial: "))
        intervalo_final: int = int(input("Digite um valor para difinir o intervalo(positivo e inteiro) Final: "))
        if intervalo_incial > intervalo_final:
            print("O valor inicial deve ser menor que o valor final!!!")
            return intervalo()
        if intervalo_incial < 0:
            print(f'Valor incorreto! {intervalo_incial}')
            return intervalo()
        return intervalo_incial, intervalo_final
    except ValueError as error:
        print(f'Valor incorreto! {error}')
        return intervalo()


def somar_valores(i: int, j: int):
    soma: int = 0
    for x in range(i, j+1):
        if x % 2 != 0:
            soma += x
    print(soma)


a, b = intervalo()
somar_valores(a, b)

