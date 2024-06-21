class Moto:

    def __init__(self, marca, modelo, cor, marcha, marcha_min, marcha_max):
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__marcha = marcha
        self.__marcha_min = marcha_min
        self.__marcha_max = marcha_max
        self.__ligada = 0

    def marcha_acima(self):
        if (self.__marcha >= self.__marcha_max):
            self.__marcha == 5
        else:
            self.__marcha += 1

    def marcha_abaixo(self):
        if (self.__marcha <= self.__marcha_min):
            self.__marcha == 0
        else:
            self.__marcha -= 1


    def show(self):
        print(f'Marca = {self.__marca}, Modelo:{self.__modelo}, '
              f'Cor: {self.__cor} e Marcha Atual: {self.__marcha},'
              f'Marcha minima: {self.__marcha_min}, Marcha maxima: {self.__marcha_max},'
              f'Ligada?: {"Não" if self.__ligada == 0 else "Sim"}')


def main():
    moto = Moto('Honda','1234', 'Preta',1, 1, 5)

    moto.show()
    moto.marcha_acima()
    moto.marcha_acima()
    moto.marcha_abaixo()
    moto.show()


if __name__ == "__main__":
    main()

