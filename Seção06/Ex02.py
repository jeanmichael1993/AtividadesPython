
def abrir_arquivo() -> str:
    try:
        with open('arq.txt', 'r') as arquivo:
            dados = arquivo.readlines()
        return dados
    except ValueError as error:
        print('error')


if __name__ == "__main__":
    dados: str = abrir_arquivo()
    print(f'A quantidade de linhas é de: {len(dados)}')
