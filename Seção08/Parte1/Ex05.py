
class Retangulo:

    def __init__(self):
        self.__comprimento = 0
        self.__largura = 0
        self.__area = 0
        self.__perimetro = 0

    def set_comprimento(self, comprimento):
        self.__comprimento = comprimento

    def set_largura(self, largura):
        self.__largura = largura

    def calcular_area(self):
        self.__area = self.__comprimento * self.__largura
        pass

    def calcuar_perimetro(self):
        self.__perimetro = (self.__comprimento * 2) + (self.__largura * 2)
        pass

    def show(self) -> str:
        self.calcuar_perimetro()
        self.calcular_area()
        return print(f"O comprimento é:{self.__comprimento}, a largura é:{self.__largura}, a area é :{self.__area},  e o perimetro é : {self.__perimetro}")


def main():
    retangulo = Retangulo()
    retangulo.set_largura(4)
    retangulo.set_comprimento(5)
    retangulo.show()


if __name__ == "__main__":
    main()
