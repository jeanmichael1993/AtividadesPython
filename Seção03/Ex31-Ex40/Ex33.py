def obter_dados() -> int:
    try:
        n: int = int(input("Digite o valor de N: "))
        i: int = int(input("Digite o valor de I: "))
        j: int = int(input("Digite o valor de J: "))
        if n <= 0 or i <= 0 or j <= 0:
            mostrar_error(n, "N") if n <= 0 else (mostrar_error(i, "I") if i <= 0 else mostrar_error(j, "J"))
            return obter_dados()
        return n, i, j
    except ValueError as error:
        print(f'Valor digitado está incorreto!{error}')
        return obter_dados()


def mostrar_error(valor: int, letra: str) -> str:
    print(f'O valor de {letra} está incorreto! : {valor}')


def imprimir_naturais(n: int, i: int, j: int):
    count: int = 0
    t: int = 1
    while count < n:
        if t % i == 0 or t % j == 0:
            print(t, end=',') if count < n-1 else print(t, end='')
            count += 1
        t += 1


a, b, c = obter_dados()
imprimir_naturais(a, b, c)
