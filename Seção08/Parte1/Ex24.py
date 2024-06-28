
class Televisor:

    def __init__(self, ligado, canal, volume):
        self.__ligado = ligado
        self.__canal = canal
        self.__volume = volume
        self.__numCanais = 3
        self.__volumeMax = 100

    def on(self):
        self.__ligado = 1

    def off(self):
        self.__ligado = 0

    def channel_up(self):
        if self.__canal < self.__numCanais:
            self.__canal += 1
        elif self.__canal == self.__numCanais:
            self.__canal = 1

    def channel_down(self):
        if self.__canal > 1:
            self.__canal -= 1
        elif self.__canal == 1:
            self.__canal = self.__numCanais

    def show(self):
        print(f'A TV está : {"Ligada" if self.__ligado == 1 else "Desligada"}, '
              f'O canal está no: {self.__canal}, '
              f'O volume é:{self.__volume}, '
              f'O número maximo de canais é: {self.__numCanais}, '
              f'O volume maximo é : {self.__volumeMax}')


def main():
    tv = Televisor(1, 1, 10)
    tv.show()
    tv.channel_down()
    tv.show()
    tv.channel_down()
    tv.show()
    tv.channel_down()
    tv.show()
    tv.channel_down()
    tv.show()


if __name__ == "__main__":
    main()
