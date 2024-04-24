class Moto:

    def __init__(self, marca, modelo, cor, marcha):
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__marcha = marcha

    def show(self):
        print(f'Marca = {self.__marca}, Modelo:{self.__modelo}, Cor: {self.__cor} e Marcha Atual: {self.__marcha}')


def main():
    moto = Moto('Honda','1234', 'Preta','1')
    moto.show()


if __name__ == "__main__":
    main()

