
def abrir_arquivo(nome: str) -> str:
    try:
        dados: str = ''
        with open(nome+'.txt', 'r') as arquivo:
            dados = arquivo.readlines()
        return dados
    except TypeError as error:
        print(error)

def tratar_dados(dados: str) -> str:
    dados_tratados: str = []
    for i in dados:
        nome = (i[:40]).rstrip()
        nota = (i[40:]).replace("\n",'')
        dados_tratados.append([nome, nota])
    return dados_tratados


def guardar_dados(dados: str, nome: str):
    try:
        with open(nome+'.txt', 'w+') as arquivo:
            alunos: str = {}
            for i in dados:
                alunos.update({i[0]: i[1]})
            alunos = dict(sorted(alunos.items()))
            for chave, valor in alunos.items():
                arquivo.write(f'{chave} = {valor}\n')
    except TypeError as error:
        print(error)


if __name__ == "__main__":
    try:
        nome_arquivo: str = input("Digite o nome do arquivo: ")
        nome_arquivo_saida: str = input("Digite o nome do arquivo de saida: ")
        dados: str = abrir_arquivo(nome_arquivo)
        dados_tratados: str = tratar_dados(dados)
        guardar_dados(dados_tratados, nome_arquivo_saida)
    except TypeError as error:
        print(error)