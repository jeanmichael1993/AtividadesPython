

if __name__ == "__main__":
    try:
        with open("arq.txt", 'w+') as arquivo:
            caracter: str = ''
            while caracter != '0':
                caracter = input("Digite o caracter: ")
                arquivo.write(caracter)
    except ValueError as error:
        print("error")


with open("arq.txt",'r') as arquivo:
    print(arquivo.read())

