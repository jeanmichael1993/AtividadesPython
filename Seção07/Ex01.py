
class Pessoa:

    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_idade(self):
        return self.__idade

    def set_idade(self, idade):
        self.__idade = idade

    def get_altura(self):
        return self.__altura

    def show_person(self):
        return print(f"{self.__nome} tem {self.__idade} anos e sua altura é de: {self.__altura}")


def main():
    pessoas: str = []
    for i in range(3):
        nome: str = input("Digite o nome da pessoa: ")
        idade: str = input("Digite a idade da pessoa: ")
        altura: str = input("Digite a altura da pessoa: ")
        pessoas.append(Pessoa(nome, idade, altura))

    for i in pessoas:
        i.show_person()


if __name__ == "__main__":
    main()