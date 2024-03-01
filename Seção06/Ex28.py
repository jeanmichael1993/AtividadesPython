

def abrir_arquivo(arquivo_entrada: str) -> str:
    try:
        dados: str = ''
        with open(arquivo_entrada + '.txt', 'r') as arquivo:
            dados = arquivo.readlines()
        return dados
    except TypeError as error:
        print(error)


def tratar_dados(dados: str) -> str:
    dados_tratados: str = []
    for i in dados:
        dados_tratados.append(i.rstrip().replace("\n", ''))
    return dados_tratados


def guardar_dados(arquivo_saida: str, dados_tratados):
    try:
        dados_invertidos: str = dados_tratados[::-1]
        dados_trocados: str = [x[::-1] for x in dados_invertidos]
        with open(arquivo_saida + '.txt', 'w+') as arquivo:
            for x in dados_trocados:
                arquivo.write(f'{x.capitalize()}\n')
    except ValueError as error:
        print(error)


def main():
    arquivo_entrada: str = input("Digite o nome do arquivo de entrada:")
    dados: str = abrir_arquivo(arquivo_entrada)
    dados_tratados: str = tratar_dados(dados)
    arquivo_saida: str = input("Digite o nome do arquivo de saida:")
    guardar_dados(arquivo_saida, dados_tratados)


if __name__ == "__main__":
    main()