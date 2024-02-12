from collections import Counter

def ler_arquivo() -> str:
    try:
        dados: str = ''
        with open('teste2.txt','r', encoding='UTF-8') as arquivo:
            dados = (arquivo.read().replace('\n', ' ')).split(" ")
        return dados
    except:
        print(error)


if __name__ == "__main__":
    try:
        palavra: str = input("Digite a palavra buscada: ")
        dados: str = ler_arquivo()
        contar = Counter(dados)
        print(f'{f'A palavra "{palavra}" aparece {contar.get(palavra)} vezes'  if contar.get(palavra, 0) != 0 else 'Palavra não existe!'}')
    except ValueError as error:
        print(error)