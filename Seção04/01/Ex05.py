def ler_valor() -> int:
    valores: int = []
    for x in range(10):
        try:
            valores.append(int(input("Digite um valor inteiro: ")))
        except ValueError as error:
            print(error)
            return ler_valor()
    return valores

pares: int = 0
valores: int = ler_valor()
for x in valores:
    if x % 2 == 0: 
        pares += 1

print(pares)