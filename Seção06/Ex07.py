
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
                if ord((i).lower()) in [97, 225, 224, 226, 227, 228, 229, 101, 232, 233, 234, 235, 105, 236, 237, 238, 239, 111, 242, 243, 244, 245, 246
                                ,117, 249, 250, 251, 252]:
                    arquivo.write('*')
                else:
                    arquivo.write(i)
    except:
        print("error!")


if __name__ == '__main__':
    dados: str = ler_arquivo()
    escrever_arquivo(dados)
