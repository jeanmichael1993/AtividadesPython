def concaternar(nome: str) -> str:
    quantidade: int = 40
    nome = nome + (" " * (quantidade - len(nome)))
    return nome


def guardar_dados(n: int):
    try:
        with open("Ex21Arq.txt", "w+") as arquivo:
            for i in range(n):
                nome_aluno: str = concaternar(input("Digite o nome do aluno: "))
                nota_final: str = (input("Digite a nota final do aluno: ")).replace(',','.')
                arquivo.write(f'{nome_aluno}{nota_final}\n')
    except TypeError as error:
        print(error)


def ler_arquivo() -> str:
    try:
        dados: str = ''
        with open('Ex21Arq.txt', 'r') as arquivo:
            dados = arquivo.readlines()
        return dados
    except TypeError as error:
        print(error)


def tratar_dados(dados: str) -> str:
    dados_tratados: str = []
    for i in dados:
        nome = (i[:40]).rstrip()
        nota = (i[40:]).replace("\n", '')
        dados_tratados.append([nome, nota])
    return dados_tratados


if __name__ == "__main__":
    try:
        n: int = int(input("Entre com o número de alunos de uma disciplina: "))
        guardar_dados(n)
        dados: str = ler_arquivo()
        dados_tratados: str = tratar_dados(dados)
        maior_nota: float = 0
        nome_maior_nota: str = ''
        for i in dados_tratados:
            if float(i[1]) > maior_nota:
                maior_nota = float(i[1])
                nome_maior_nota = i[0]
        print(f"A maior nota é de: {maior_nota}, do aluno: {nome_maior_nota}")
    except TypeError as error:
        print(error)
        
