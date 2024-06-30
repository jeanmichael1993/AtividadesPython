class Equipamento:

    def __init__(self, A, B):
        self.__atributo_a = A
        self.__atributo_b = B

    def set_atributo_a(self, valor):
        self.__atributo_a = valor

    def get_atributo_a(self):
        return self.__atributo_a

    def set_atributo_b(self, valor):
        self.__atributo_b = valor

    def get_atributo_b(self):
        return self.__atributo_b

    def show(self):
        return f'Atributo A: {self.get_atributo_a()}, Atributo B: {self.get_atributo_b()}'


class Computador(Equipamento):

    def __init__(self, A, B, C, D):
        super().__init__(A, B)
        self.__atributo_c = C
        self.__atributo_d = D

    def get_atributo_c(self):
        return self.__atributo_c

    def set_atributo_c(self, valor):
        self.__atributo_c = valor

    def get_atributo_d(self):
        return self.__atributo_d

    def set_atributo_d(self, valor):
        self.__atributo_d = valor

    def show(self):
        return (f'{super().show()}, '
                f'Atributo C: {self.get_atributo_c()}, Atributo D: {self.get_atributo_d()}')

class Testa_equipamento:

    @staticmethod
    def main():
        teste = Equipamento(4, 5)
        teste2 = Computador(teste.get_atributo_a(), teste.get_atributo_b(), 6, 7)

        print(teste.show())
        print(teste2.show())


if __name__ == "__main__":
    Testa_equipamento.main()
