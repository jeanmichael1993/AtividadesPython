
def calculo_conceito(nota_aluno: float, frequencia_aluno: int):
    if frequencia_aluno <= 20:
        if 9.0 <= nota_aluno <= 10.0:
            print("A")
        elif 7.5 <= nota_aluno <= 8.9:
            print("B")
        elif 5.0 <= nota_aluno <= 7.4:
            print("C")
        elif 4.0 <= nota_aluno <= 4.9:
            print("D")
        elif 0.0 <= nota_aluno <= 3.9:
            print("E")
    elif frequencia_aluno > 20:
        if 9.0 <= nota_aluno <= 10.0:
            print("B")
        elif 7.5 <= nota_aluno <= 8.9:
            print("C")
        elif 5.0 <= nota_aluno <= 7.4:
            print("D")
        elif 4.0 <= nota_aluno <= 4.9:
            print("E")
        elif 0.0 <= nota_aluno <= 3.9:
            print("E")


nota_aluno: float = float(input("Digite a nota do aluno: "))
frequencia_aluno: int = int(input("Digite a quantidade de faltas do aluno: "))


calculo_conceito(nota_aluno, frequencia_aluno)