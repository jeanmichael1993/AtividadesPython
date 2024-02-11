def ler_arquivo() -> str:
    try:
        dados: str = ''
        with open('arq.txt', 'r') as arquivo:
            dados = arquivo.read()
        return dados
    except:
        print('error')


def quantidade(n: str, dados: str) -> int:
    count: int = 0
    for i in dados:
        if i.upper() == n.upper():
            count += 1
    return count


if __name__ == "__main__":
    dados: str = ler_arquivo()
    n: str = input("Digite o caracter desejado: ")
    qtd: int = quantidade(n, dados)
    print(f'A quantidade de "{n}" é: {qtd}')

