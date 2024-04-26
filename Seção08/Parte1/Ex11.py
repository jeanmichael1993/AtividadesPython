class Moto:

    def __init__(self, marca, modelo, cor, marcha):
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__marcha = marcha

    def marcha_acima(self):
        if (self.__marcha >= 5):
            self.__marcha == 5
        else:
            self.__marcha += 1

    def marcha_abaixo(self):
        if (self.__marcha <= 0):
            self.__marcha == 0
        else:
            self.__marcha -= 1

    def show(self):
        print(f'Marca = {self.__marca}, Modelo:{self.__modelo}, Cor: {self.__cor} e Marcha Atual: {self.__marcha}')


def main():
    moto = Moto('Honda','1234', 'Preta',1)

    moto.show()
    moto.marcha_acima()
    moto.marcha_acima()
    moto.marcha_abaixo()
    moto.show()


if __name__ == "__main__":
    main()

