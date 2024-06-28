
class Televisor:

    def __init__(self, ligado, canal, volume):
        self.__ligado = ligado
        self.__canal = canal
        self.__volume = volume
        self.__numCanais = 10
        self.__volumeMax = 100

    def on(self):
        self.__ligado = 1

    def off(self):
        self.__ligado = 0

    def show(self):
        print(f'A TV está : {"Ligada" if self.__ligado == 1 else "Desligada"}, '
              f'O canal está no: {self.__canal}, '
              f'O volume é:{self.__volume}, '
              f'O número maximo de canais é: {self.__numCanais}, '
              f'O volume maximo é : {self.__volumeMax}')


def main():
    tv = Televisor(1, 10, 10)
    tv.show()
    tv.off()
    tv.show()
    tv.on()
    tv.show()


if __name__ == "__main__":
    main()
