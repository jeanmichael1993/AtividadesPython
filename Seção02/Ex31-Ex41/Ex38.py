def entrada_valores(dia: int, mes: int, ano: int):
    valores_testados: bool = teste_valores(dia, mes, ano)
    if valores_testados == 1:
        print("Data válida!")
    elif valores_testados == 0:
        print("Data Inválida!")


def teste_valores(dia: int, mes: int, ano: int):
    if mes == 2:
        if int(ano) % 4 == 0:
            if dia <= 0 or dia > 29:
                return 0
        else:
            if dia <= 0 or dia > 28:
                return 0
    else:
        if mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if dia <= 0 or dia > 30:
                return 0
        else:
            if dia <= 0 or dia > 31:
                return 0
    if mes < 0 or mes > 13:
        return 0
    if ano > 2008:
        return 0
    return 1


data_nascimento: str = input("Digite seu ano de nascimento separado por '/': ").split('/')
dia: int = int(data_nascimento[0])
mes: int = int(data_nascimento[1])
ano: int = int(data_nascimento[2])
entrada_valores(dia, mes, ano)

