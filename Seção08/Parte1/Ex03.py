class Quadrado:

    def __init__(self):
        self.__lado = 0
        self.__area = 0
        self.__perimetro = 0

    def set_lado(self, lado):
        self.__lado = lado

    def calcular_area(self):
        self.__area = self.__lado * self.__lado

    def calcular_perimetro(self):
        self.__perimetro = self.__lado * 4

    def show(self):
        print(f"Aréa é :{self.__area}, o valor do perimetro é {self.__perimetro}, e valor do lado: {self.__lado}")


def main():
    quadrado = Quadrado()
    quadrado.set_lado(4)
    quadrado.calcular_area()
    quadrado.calcular_perimetro()
    quadrado.show()


if __name__ == "__main__":
    main()