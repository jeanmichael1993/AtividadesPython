
def guardar_dados(nome: str, telefone: str):
    try:
        with open('arqEx13.txt', 'a') as arquivo:
            arquivo.write(nome + ' ' + telefone + "\n")
    except TypeError as error:
        print(error)


if __name__ == "__main__":
    nome: str = 0
    telefone: str = '-1'
    while telefone != '0':
        nome = input("Digite um nome: ")
        telefone = input("Digite um telefone: ")
        if telefone == '0':
            break
        guardar_dados(nome, telefone)


