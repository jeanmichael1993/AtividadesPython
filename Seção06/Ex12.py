

def ler_arquivo(nome: str) -> str:
    try:
        dados: str = ''
        with open(nome, 'r', encoding='iso8859-2') as arquivo:
            dados = arquivo.readlines()
        return dados
    except:
        print(error)


def guardar_dados(nome: str, dados: str):
    try:
        dadosTratados: str = {}
        mais_populosa: str = ''
        qtd_polulosa: float = 0
        for i in dados:
            chave, valor = i.split(';')
            valor = (valor.replace('\n', '')).replace(',', '.')
            dadosTratados.update({chave: valor})
        for chave, valor in dadosTratados.items():
            if float(valor) > qtd_polulosa:
                qtd_polulosa = float(valor)
                mais_populosa = chave
        print(mais_populosa, qtd_polulosa)
        with open(nome, 'w+', encoding='iso8859-2') as arquivo:
            arquivo.write(f'A cidade mais populosa é: {mais_populosa} com {qtd_polulosa} habitantes!')
    except TypeError as error:
        print(error)


if __name__ == "__main__":
    try:
        nome: str = input("Digite o nome do arquivo com extensão: ")
        dados: str = ler_arquivo(nome)
        nomeArquivoFinal: str = input("Digite o nome do arquivo para salvar os dados: ")
        guardar_dados(nomeArquivoFinal, dados)
    except ValueError as error:
        print(error)