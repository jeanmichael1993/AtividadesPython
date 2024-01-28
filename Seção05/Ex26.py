
def soma(valor):
    soma: int = 0
    for i in range(1, valor+1):
        soma += i
    return soma


if __name__ == "__main__":
    try:
        valor: int = int(input("Digite um valor: "))
        print(soma(valor))
    except ValueError as error:
        print('valor errado!')
