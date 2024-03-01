import os

def criar_arquivo():
    with open("registros.txt", "w+") as arquivo:
        arquivo.write("")

def incluir_registro():
    codigo_vendedor = input("Digite o c�digo do vendedor: ")
    nome_vendedor = input("Digite o nome do vendedor: ")
    valor_venda = float(input("Digite o valor da venda: "))
    mes = input("Digite o m�s: ")

    registro = f"{codigo_vendedor},{nome_vendedor},{valor_venda},{mes}\n"

    with open("registros.txt", "a") as arquivo:
        arquivo.write(registro)

    print("Registro inclu�do com sucesso.")

def excluir_registro():
    codigo_vendedor = input("Digite o c�digo do vendedor a ser exclu�do: ")
    mes = input("Digite o m�s do registro a ser exclu�do: ")

    with open("registros.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    with open("registros.txt", "w") as arquivo:
        for linha in linhas:
            campos = linha.strip().split(',')
            if campos[0] != codigo_vendedor or campos[3] != mes:
                arquivo.write(linha)

    print("Registro exclu�do com sucesso.")

def alterar_valor_venda():
    codigo_vendedor = input("Digite o c�digo do vendedor: ")
    mes = input("Digite o m�s do registro a ser alterado: ")

    with open("registros.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    with open("registros.txt", "w") as arquivo:
        for linha in linhas:
            campos = linha.strip().split(',')
            if campos[0] == codigo_vendedor and campos[3] == mes:
                novo_valor = float(input(f"Digite o novo valor da venda para {codigo_vendedor}/{mes}: "))
                campos[2] = str(novo_valor)
                linha = ','.join(campos) + '\n'
            arquivo.write(linha)

    print("Valor da venda alterado com sucesso.")

def imprimir_registros():
    with open("registros.txt", "r") as arquivo:
        for linha in arquivo:
            print(linha.strip())

def excluir_arquivo():
    try:
        os.remove("registros.txt")
        print("Arquivo exclu�do com sucesso.")
    except FileNotFoundError:
        print("Arquivo n�o encontrado.")

def main():
    while True:
        print("\nMenu:")
        print("1. Criar o arquivo de dados")
        print("2. Incluir um determinado registro no arquivo")
        print("3. Excluir um determinado vendedor no arquivo")
        print("4. Alterar o valor de uma venda no arquivo")
        print("5. Imprimir os registros na sa�da padr�o")
        print("6. Excluir o arquivo de dados")
        print("7. Finalizar o programa")

        opcao = input("Digite a op��o desejada: ")

        if opcao == "1":
            criar_arquivo()
        elif opcao == "2":
            incluir_registro()
        elif opcao == "3":
            excluir_registro()
        elif opcao == "4":
            alterar_valor_venda()
        elif opcao == "5":
            imprimir_registros()
        elif opcao == "6":
            excluir_arquivo()
        elif opcao == "7":
            break
        else:
            print("Op��o inv�lida. Tente novamente.")

if __name__ == "__main__":
    main()






