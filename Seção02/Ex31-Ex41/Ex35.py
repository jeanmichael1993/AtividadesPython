
def validar_data(data_lida: str):
    if int(data_lida[1]) == 2:
        if int(data_lida[2]) % 4 == 0:
            if int(data_lida[0]) < 1 or int(data_lida[0]) > 29:
                print("data errada!")
            if int(data_lida[1]) < 1 or int(data_lida[1]) > 12:
                print("mês errado!")
        else:
            if int(data_lida[0]) < 1 or int(data_lida[0]) > 28:
                print("data errada!")
            if int(data_lida[1]) < 1 or int(data_lida[1]) > 12:
                print("mês errado!")
    else:
        if int(data_lida[0]) < 1 or int(data_lida[0]) > 31:
            print("data errada!")
        if int(data_lida[1]) < 1 or int(data_lida[1]) > 12:
            print("mês errado!")


data_lida: str = input("Digite a data entre '/' :").split("/")

validar_data(data_lida)