from collections import Counter


def ler_arquivo() -> str:
    try:
        dados: str = ''
        with open('arq.txt', 'r') as arquivo:
            dados = arquivo.read()
        return dados
    except:
        print("Error!")


if __name__ == "__main__":
    dados: str = ler_arquivo()
    resultado: str = Counter(dados)
    for chave, valor in resultado.items():
        if chave != '' and chave != '\n':
            print(f'letra:{chave}, quantidade: {valor}')

