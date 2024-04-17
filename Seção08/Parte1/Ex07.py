
class Cirulo:

    def __init__(self):
        self.__raio = 0
        self.__area = 0
        self.__perimetro = 0

    def set_raio(self, raio):
        self.__raio = raio

    def set_area(self, area):
        self.__area = area

    def set_perimetro(self, perimetro):
        self.__perimetro = perimetro

    def calcular_area(self):
        self.set_area(3.14 * self.__raio * self.__raio)

    def calcular_perimetro(self):
        self.set_perimetro(2 * 3.14 * self.__raio)

    def show(self):
        self.calcular_area()
        self.calcular_perimetro()
        return print(f"O raio é:{self.__raio}, a area é:{self.__area} e o perimetro é :{self.__perimetro}.")


def main():
    circulo = Cirulo()
    circulo.set_raio(4)
    circulo.show()


if __name__ == "__main__":
    main()