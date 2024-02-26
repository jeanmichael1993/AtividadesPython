
def ler_dados(n: int) -> str:
    try:
        funcionario: str = {}
        for i in range(n):
            funcao: str = input("Digite a profissão do funcionario: ")
            tempo_servico: str = input("Digite quantos anos de tempo de serviço do funcionario: ")
            funcionario.update({funcao:tempo_servico})
        return funcionario
    except TypeError as error:
        print(error)


def guardar_dados(funcionarios:str ):
    try:
        with open("emp.txt", 'w+') as arquivo:
            for chave, valor in funcionarios.items():
                arquivo.write(f'Profissão: {chave}, tem de serviço em anos: {valor}\n')
    except TypeError as error:
        print(error)


if __name__ == "__main__":
    n: int = 5
    funcionarios: str = ler_dados(n)
    guardar_dados(funcionarios)

