
class Pessoa:

    def __init__(self, cod: int, name: str, year_old: int):
        self.__cod = cod
        self.__name = name
        self.__year_old = year_old

    def get_cod(self):
        return self.__cod

    def get_name(self):
        return self.__name

    def get_year(self):
        return self.__year_old

    def show(self, *args: int):
        """
        Show all atributos
        :param value: value to age
        :return: all atributos
        """
        if len(args) == 1:
            if args[0] == 1:
                return f'Cod: {self.get_cod()}, Name: {self.get_name()}, Age: {self.get_year()}'
            else:
                return f'Cod: {self.get_cod()}, Name: {self.get_name()}'
        else:
            return f'Cod: {self.get_cod()}, Name: {self.get_name()}, Age: {self.get_year()}'


class Test_Pessoa:
    pessoa = Pessoa(1, 'teste', 20)
    print(pessoa.show())
    print(pessoa.show(2))
    print(pessoa.show(1))
    print(pessoa.show(4))

