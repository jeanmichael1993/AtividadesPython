
class Agenda:

    def __init__(self, lista_pessoas: str):
        """
        Adiciona uma lista de listas de pessoas na variavel.
        :param lista_pessoas: lista de listas de pessoas.
        """
        self.__lista_pessoa = lista_pessoas

    def armazena_pessoa(self, nome: str, idade: int, altura: float):
        """
        :param nome: nome da pessoa
        :param idade: idade da pessoa
        :param altura: altura da pessoa
        :return: nada
        """
        self.__lista_pessoa.append([nome, idade, altura])

    def remove_pessoa(self, nome: str):
        """
        Remove um item da lista
        :param nome: nome da pessoa que vai retirar da lista
        :return: nada
        """
        for i in self.__lista_pessoa:
            if i[0].upper() == nome.upper():
                del self.__lista_pessoa[self.__lista_pessoa.index(i)]

    def busca_pessoa(self, nome: str) -> str:
        """
        busca pessoa na lista pelo nome
        :param nome: nome que está sendo buscado
        :return: dados da pessoa buscada
        """
        for i in self.__lista_pessoa:
            if i[0].upper() == nome.upper():
                return print(f'Dados buscados (index na agenda): {self.__lista_pessoa.index(i)}')
        return print("Nome não encontrado!")

    def imprimir_agenda(self) -> str:
        """
        :return: dados da lista
        """
        return [print(f'{i}') for i in self.__lista_pessoa]

    def imprimir_pessoa(self, index) -> str:
        """
        imprimi dados da pessoa solicitada
        :param index: posição da pesssoa solicitada
        :return: dados do index solicitado
        """
        for i in self.__lista_pessoa:
            if self.__lista_pessoa.index(i) == index:
                return print(f'Pessoas buscada por index: {i}')
        return print("Não encontrado!")


def main():
    pessoas: str = [['jean', 18, 1.80], ['teste1', 20, 1.75], ['teste2', 20, 1.79], ['teste3', 30, 1.67]]
    agenda_pessoas = Agenda(pessoas)
    agenda_pessoas.armazena_pessoa('teste4', 31, 1.87)
    agenda_pessoas.remove_pessoa('teste2')
    agenda_pessoas.busca_pessoa('jean')
    agenda_pessoas.imprimir_agenda()
    agenda_pessoas.imprimir_pessoa(2)


if __name__ == "__main__":
    main()

