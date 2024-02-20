def buscar_dados(n: int) -> str:
    try:
        vetorA: str = []
        vetorB: str = []
        for i in range(n):
            vetorA.append(input(f"Digite o nome do {i+1}º aluno: "))
            vetorB.append(input(f"Digite a nota final do {i+1}º aluno: "))
        return vetorA, vetorB
    except TypeError as error:
        print(error)


def concatenar_com_espacos(strings):
    resultado = strings
    comprimento_desejado = 40
    espacos_adicionais = ' ' * max(comprimento_desejado - len(resultado), 0)
    resultado += espacos_adicionais
    return resultado


def inserir_dados(vetA: str, vetB: str):
    try:
        with open('Ex20arq.txt', 'a+') as arquivo:
            for i, j in zip(vetA, vetB):
                arquivo.write(f"{concatenar_com_espacos(i)}{j}\n")
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    n: int = int(input("Digite o número de alunos: "))
    vetA, vetB = buscar_dados(n)
    inserir_dados(vetA, vetB)


