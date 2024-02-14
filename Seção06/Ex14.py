import datetime

def abrir_arquivo() -> str:
    try:
        dados: str = ''
        with open('arqEx14.txt', 'r') as arquivo:
            dados = arquivo.readlines()
        return dados
    except TypeError as error:
        print(error)

def escrever_arquivo(dados: str):
    try:
        for i in dados:
            i = i.rstrip().replace('\n',' ').split(" ")
        for i in dados:
            if len(i) > 1:
                nome, dia, mes, ano = i.split()
                data_hoje = datetime.datetime.today().year
                aniversario = datetime.datetime(year=int(ano), month =int(mes), day = int(dia)).year
                print(data_hoje)
                print(aniversario)
                idade = (data_hoje - aniversario)
                with open('arqEx14Resultado.txt', 'a+') as arquivo:
                    arquivo.write(nome + " " + str(idade) + '\n' )
    except TypeError as error:
        print(error)


if __name__ == "__main__":
    dados: str = abrir_arquivo()
    escrever_arquivo(dados)