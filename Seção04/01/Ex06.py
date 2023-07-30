def ler_valor() -> int:
    valores: int = []
    for x in range(10):
        try:
            valores.append(int(input("Digite um valor inteiro: ")))
        except ValueError as error:
            print(error)
            return ler_valor()
    return valores


valores: int = ler_valor()
print(f"O valor minimo é {min(valores)} e o valor maximo é {max(valores)}.")

