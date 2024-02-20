def ler_arquivo() -> str:
    try:
        dados: str = ''
        with open("arqEx19.txt", 'r') as arquivo:
            dados = arquivo.readlines()
        return dados
    except TypeError as error:
        print(error)


def tratar_dados(dados: str) -> str:
    try:
        dados_tratados: str = []
        [dados_tratados.append(i.rstrip().replace("\n",'')) for i in dados if len(i) > 1]
        return dados_tratados
    except TypeError as error:
        print(error)


def maior_nota(dados_tratados: str) -> str:
    try:
        alunos_dict: str = {}
        for i in dados_tratados:
            a, b = i.split(" ")
            alunos_dict.update({a[5:]: b[5:]})
        maior_nota: int = 0
        aluno_maior_nota: str = ''
        for chave, valor in alunos_dict.items():
            if int(valor) > maior_nota:
                maior_nota = int(valor)
                aluno_maior_nota = chave
        return maior_nota, aluno_maior_nota
    except TypeError as error:
        print(error)


if __name__ == "__main__":
    dados: str = ler_arquivo()
    dados_tratados: str = tratar_dados(dados)
    nota, aluno = maior_nota(dados_tratados)
    print(f"O(a) Aluno(a) com a maior nota é o(a): {aluno}, com a nota:{nota}")

