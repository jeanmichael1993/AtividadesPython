def quadrado_perfeito(numero: int) -> int:
    try:
        valor = numero ** 2
        if valor // 2 != 0:
            return "É um quadrado perfeito!"
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    numero: int = int(input("Digite um numero inteiro: "))
    res = quadrado_perfeito(numero)
    print(res)

