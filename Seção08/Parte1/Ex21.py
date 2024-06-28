
class Televisor:

    def __init__(self, ligado, canal, volume):
        self.__ligado = ligado
        self.__canal = canal
        self.__volume = volume

    def show(self):
        print(f'A TV está : {"Ligada" if self.__ligado == 1 else "Desligada"},'
              f'O canal está no: {self.__canal},'
              f'O volume é:{self.__volume}')


def main():
    tv = Televisor(1,10,10)
    tv.show()


if __name__ == "__main__":
    main()