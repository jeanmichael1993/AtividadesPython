conjunto: int = []
for x in range(10):
    try:
        conjunto.append(int(input("Digite um número inteiro real: ")))
    except ValueError as error:
        print(error)

novo_conjunto: int = [x ** 2 for x in conjunto]
print(novo_conjunto)