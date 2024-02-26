import pickle

class Despensa:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, codigo, descricao, quantidade):
        if codigo in self.produtos:
            self.produtos[codigo]['quantidade'] += quantidade
        else:
            self.produtos[codigo] = {'descricao': descricao, 'quantidade': quantidade}

    def retirar_produto(self, codigo, quantidade):
        if codigo in self.produtos:
            if quantidade <= self.produtos[codigo]['quantidade']:
                self.produtos[codigo]['quantidade'] -= quantidade
                if self.produtos[codigo]['quantidade'] == 0:
                    del self.produtos[codigo]
                return True
            else:
                print("Quantidade insuficiente.")
        else:
            print("Produto n�o encontrado.")
        return False

    def relatorio_geral(self):
        print("Relat�rio Geral:")
        for codigo, produto in self.produtos.items():
            print(f"C�digo: {codigo}, Descri��o: {produto['descricao']}, Quantidade: {produto['quantidade']}")

    def relatorio_produtos_nao_disponiveis(self):
        print("Produtos n�o dispon�veis:")
        for codigo, produto in self.produtos.items():
            if produto['quantidade'] == 0:
                print(f"C�digo: {codigo}, Descri��o: {produto['descricao']}")

    def salvar_despensa(self, nome_arquivo):
        with open(nome_arquivo, 'wb') as arquivo:
            pickle.dump(self.produtos, arquivo)

    def carregar_despensa(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'rb') as arquivo:
                self.produtos = pickle.load(arquivo)
        except FileNotFoundError:
            print("Arquivo n�o encontrado. Criando uma nova despensa.")

# Fun��o principal
def main():
    despensa = Despensa()
    arquivo_despensa = 'despensa.bin'

    despensa.carregar_despensa(arquivo_despensa)

    while True:
        print("\nOp��es:")
        print("1. Adicionar Produto")
        print("2. Retirar Produto")
        print("3. Relat�rio Geral")
        print("4. Relat�rio Produtos N�o Dispon�veis")
        print("5. Sair")

        opcao = input("Escolha uma op��o (1-5): ")

        if opcao == '1':
            codigo = int(input("Digite o c�digo do produto: "))
            descricao = input("Digite a descri��o do produto: ")
            quantidade = int(input("Digite a quantidade a ser adicionada: "))
            despensa.adicionar_produto(codigo, descricao, quantidade)
        elif opcao == '2':
            codigo = int(input("Digite o c�digo do produto: "))
            quantidade = int(input("Digite a quantidade a ser retirada: "))
            despensa.retirar_produto(codigo, quantidade)
        elif opcao == '3':
            despensa.relatorio_geral()
        elif opcao == '4':
            despensa.relatorio_produtos_nao_disponiveis()
        elif opcao == '5':
            despensa.salvar_despensa(arquivo_despensa)
            print("Programa encerrado.")
            break
        else:
            print("Op��o inv�lida. Tente novamente.")


if __name__ == "__main__":
    main()
