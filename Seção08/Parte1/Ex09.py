class Moto:

    def __init__(self):
        self.__marca = 0
        self.__modelo = 0
        self.__cor = 0
        self.__marcha = 0

    def set_marca(self, marca):
        self.__marca = marca

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def set_cor(self, cor):
        self.__cor = cor

    def set_marcha(self, marcha):
        self.__marcha = marcha

    def show(self):
        print(f'Marca = {self.__marca}, Modelo:{self.__modelo}, Cor: {self.__cor} e Marcha Atual: {self.__marcha}')


def main():
    moto = Moto()
    moto.set_marca('Honda')
    moto.set_modelo('1234')
    moto.set_cor("Preta")
    moto.set_marcha('2')
    moto.show()


if __name__ == "__main__":
    main()

