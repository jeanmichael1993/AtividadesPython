
def abrir_arquivo():
    try:
        dados: str = ''
        with open("arqEx18.txt", 'r') as arquivo:
            dados = arquivo.readlines()
        return dados
    except TypeError as error:
        print(error)


def tratar_dados(dados: str) -> str:

    novos_dados: str = []
    for i in dados:
        novos_dados.append(i.rstrip().replace("\n",' ').split(" "))
    return novos_dados

def guardar_dados(dados_tratados: str):
    try:
        soma: float = 0.0
        for i in dados_tratados:
            soma += float(i[1])
        with open("arqEx18Res.txt", 'w+') as arquivo:
            arquivo.write(f"O valor total da compra foi : R$ {soma}")

    except TypeError as error:
        print(error)


if __name__ == "__main__":
    dados: str = abrir_arquivo()
    dados_tratados = tratar_dados(dados)
    guardar_dados(dados_tratados)
    for i in dados:
        print(i)