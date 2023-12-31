count: int = 4


def guardar_dados(dados_alunos, count: int):
    try:
        for x in range(count):
            aluno_cod: int = int(input("Digite o codigo do aluno: "))
            aluno_altura: float = float(input("Digite a altura do aluno: "))
            count -= 1
            dados_alunos.update({aluno_cod: aluno_altura})
        return dados_alunos
    except ValueError as error:
        print("Valor digitado está errado!")
        return guardar_dados(dados_alunos, count)


def maior_menor_altura(dados_alunos):
    lista_altura: float = []
    for x in dados_alunos:
        lista_altura.append(dados_alunos[x])
    maior: float = max(lista_altura)
    menor: float = min(lista_altura)
    for x in dados_alunos:
        if maior == dados_alunos[x]:
            print(f"O aluno com a maior altura é o cod.:{x} com altura: {dados_alunos[x]}")
        if menor == dados_alunos[x]:
            print(f"O aluno com a menor altura é o cod.:{x} com altura: {dados_alunos[x]}")


maior_menor_altura(guardar_dados({}, count))
