
class Aluno:

    def __init__(self, nome: str, nota1:float, nota2:float, nota3:float):
        self.__nome: str = nome
        self.__nota1: float = nota1
        self.__nota2: float = nota2
        self.__nota3: float = nota3

    def get_aluno_nome(self) -> str:
        return self.__nome

    def get_aluno_nota(self) -> float:
        return self.__nota1, self.__nota2, self.__nota3


def media_aluno(alunos: Aluno = 0) -> str:
    try:
        if alunos == 0:
            print('Lista Vazia!')
            return None
        print("Média dos alunos:\n")
        for i in alunos:
            nota1, nota2, nota3 = i.get_aluno_nota()
            print(f"Aluno: {i.get_aluno_nome()}, média: {((nota1+nota2+nota3) / 3):.2f}\n")
    except TypeError as error:
        print(error)


def exibir_aprovados(alunos: Aluno):
    try:
        print("Alunos Aprovados: \n")
        for i in alunos:
            nota1, nota2, nota3 = i.get_aluno_nota()
            if (nota1+nota2+nota3) / 3 >= 60:
                print(f"Aluno: {i.get_aluno_nome()}, está aprovado!")
    except TypeError as error:
        print(error)


def exibir_reprovados(alunos: Aluno):
    try:
        print("Alunos Reprovados: \n")
        for i in alunos:
            nota1, nota2, nota3 = i.get_aluno_nota()
            if (nota1+nota2+nota3) / 3 < 60:
                print(f"Aluno: {i.get_aluno_nome()}, está reprovado!")
    except TypeError as error:
        print(error)


def salvar_dados(alunos: Aluno):
    try:
        with open('Ex27Arq.txt', 'w+') as arquivo:
            for i in alunos:
                arquivo.write(f'Aluno: {i.get_aluno_nome()}, nota: {i.get_aluno_nota()}\n')
    except TypeError as error:
        print(error)



def main():
    lista_alunos: Aluno = []
    n: int = 0
    while n != 6:
        print("Digite um número para as seguintes opções:\n")
        print("(1) Inserir aluno e nota;")
        print("(2) Exibir alunos e médias;")
        print("(3) Exibir alunos aprovados;")
        print("(4) Exibir alunos reprovados;")
        print('(5) Salvar dados em disco;')
        print('(6) Sair do programa.\n')
        n = int(input("Opção: "))
        if n == 1:
            nome_aluno: str = input("Digite o nome do Aluno: ")
            nota_aluno1: float = float(input("Digite a 1ª nota do Aluno: "))
            nota_aluno2: float = float(input("Digite a 2ª nota do Aluno: "))
            nota_aluno3: float = float(input("Digite a 3ª nota do Aluno: "))
            lista_alunos.append(Aluno(nome_aluno, nota_aluno1, nota_aluno2, nota_aluno3))
            print("Atualizado com sucesso!")
        elif n == 2:
            media_aluno(lista_alunos)
        elif n == 3:
            exibir_aprovados(lista_alunos)
        elif n == 4:
            exibir_reprovados(lista_alunos)
        elif n == 5:
            salvar_dados(lista_alunos)
        elif n == 6:
            print('Sainda do programa!')
    lista_alunos: Aluno = []


if __name__ == "__main__":
    main()

