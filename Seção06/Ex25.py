import pickle
from datetime import datetime

class Contato:
    def __init__(self, nome, telefone, aniversario):
        self.nome = nome
        self.telefone = telefone
        self.aniversario = aniversario

    def __str__(self):
        return f"{self.nome} - {self.telefone} - {self.aniversario}"

class Agenda:
    def __init__(self):
        self.contatos = []

    def inserir_contato(self, contato):
        self.contatos.append(contato)

    def remover_contato(self, nome):
        self.contatos = [c for c in self.contatos if c.nome != nome]

    def pesquisar_contato(self, nome):
        return [c for c in self.contatos if c.nome.lower() == nome.lower()]

    def listar_contatos(self):
        for contato in self.contatos:
            print(contato)

    def listar_contatos_por_letra(self, letra):
        contatos_letra = [c for c in self.contatos if c.nome.lower().startswith(letra.lower())]
        for contato in contatos_letra:
            print(contato)

    def aniversariantes_do_mes(self, mes):
        aniversariantes = [c for c in self.contatos if c.aniversario.month == mes]
        for contato in aniversariantes:
            print(contato)

    def salvar_agenda(self, nome_arquivo):
        with open(nome_arquivo, 'wb') as arquivo:
            pickle.dump(self.contatos, arquivo)

    def carregar_agenda(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'rb') as arquivo:
                self.contatos = pickle.load(arquivo)
        except FileNotFoundError:
            print("Arquivo não encontrado. Criando uma nova agenda.")

def main():
    arquivo_agenda = 'agenda_contatos.bin'
    agenda = Agenda()
    agenda.carregar_agenda(arquivo_agenda)

    while True:
        print("\nOpções:")
        print("(a) Inserir Contato")
        print("(b) Remover Contato")
        print("(c) Pesquisar Contato pelo Nome")
        print("(d) Listar Todos os Contatos")
        print("(e) Listar Contatos por Letra")
        print("(f) Imprimir Aniversariantes do Mês")
        print("(s) Sair")

        opcao = input("Escolha uma opção: ").lower()

        if opcao == 'a':
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            aniversario = input("Aniversário (formato: dd/mm): ")
            try:
                data_aniversario = datetime.strptime(aniversario, "%d/%m")
                contato = Contato(nome, telefone, data_aniversario)
                agenda.inserir_contato(contato)
            except ValueError:
                print("Formato de data inválido. Use dd/mm.")

        elif opcao == 'b':
            nome = input("Nome do contato a ser removido: ")
            agenda.remover_contato(nome)

        elif opcao == 'c':
            nome = input("Nome do contato a ser pesquisado: ")
            contatos_encontrados = agenda.pesquisar_contato(nome)
            if contatos_encontrados:
                for contato in contatos_encontrados:
                    print(contato)
            else:
                print("Contato não encontrado.")

        elif opcao == 'd':
            agenda.listar_contatos()

        elif opcao == 'e':
            letra = input("Digite a letra inicial: ")
            agenda.listar_contatos_por_letra(letra)

        elif opcao == 'f':
            mes = int(input("Digite o número do mês: "))
            agenda.aniversariantes_do_mes(mes)

        elif opcao == 's':
            agenda.salvar_agenda(arquivo_agenda)
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
