import pickle

class Aluno:
    def __init__(self, matricula, sobrenome, ano_nascimento):
        self.matricula = matricula
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento

    def __str__(self):
        return f"Matrícula: {self.matricula}, Sobrenome: {self.sobrenome}, Ano de Nascimento: {self.ano_nascimento}"

def main():
    try:
        numero_alunos = int(input("Digite o número de alunos a serem armazenados: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        return

    alunos = []
    for _ in range(numero_alunos):
        matricula = input("Digite a matrícula do aluno: ")
        sobrenome = input("Digite o sobrenome do aluno: ")
        ano_nascimento = input("Digite o ano de nascimento do aluno: ")

        aluno = Aluno(matricula, sobrenome, ano_nascimento)
        alunos.append(aluno)

    arquivo_saida = 'alunos.dat'
    with open(arquivo_saida, 'wb') as arquivo:
        pickle.dump(alunos, arquivo)

    print(f"As informações dos {numero_alunos} alunos foram gravadas no arquivo {arquivo_saida}.")


if __name__ == "__main__":
    main()
