lista_idade: int = []
cond: bool = True
while cond:
    try:
        idade: int = int(input("Digite uma idade: "))
        if idade <= 0:
            cond = False
        else:
            lista_idade.append(idade)
    except ValueError as error:
        print(error)

print(f'{sum(lista_idade) / len(lista_idade):.2f}')