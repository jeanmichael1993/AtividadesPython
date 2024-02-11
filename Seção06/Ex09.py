
def ler_arquivo() -> str:
    try:
        dados: str = ''
        with open('arq.txt', 'r') as arquivo:
            dados = arquivo.read()
        return dados
    except:
        print("Error!")


def ler_arquivo2() -> str:
    try:
        dados: str = ''
        with open('newArq.txt', 'r') as arquivo:
            dados = arquivo.read()
        return dados
    except:
        print("Error!")


def escrever_arquivo(dados1: str, dados2:str):
    try:
        dados = dados1 + dados2
        with open('novoArq.txt', 'w+') as arquivo:
            for i in dados:
                arquivo.write(i)
    except:
        print("error!")


if __name__ == '__main__':
    dados1: str = ler_arquivo()
    dados2: str = ler_arquivo2()
    escrever_arquivo(dados1, dados2)
