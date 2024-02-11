
def ler_arquivo() -> str:
    try:
        dados: str = ''
        with open('arq.txt', 'r') as arquivo:
            dados = arquivo.read()
        return dados
    except:
        print("Error!")


def escrever_arquivo(dados: str):
    try:
        with open('newArq.txt', 'w+') as arquivo:
            for i in dados:
                arquivo.write(i.upper())
    except:
        print("error!")


if __name__ == '__main__':
    dados: str = ler_arquivo()
    escrever_arquivo(dados)
