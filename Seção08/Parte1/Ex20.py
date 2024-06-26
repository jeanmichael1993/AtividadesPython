
class Televisor:

    def __init__(self):
        self.__ligado = 0
        self.__canal = 0
        self.__volume = 0

    def show(self):
        print(f'A TV está : {"Ligada" if self.__ligado == 1 else "Desligada"},'
              f'O canal está no: {self.__canal},'
              f'O volume é:{self.__volume}')


def main():
    tv = Televisor()
    tv.show()


if __name__ == "__main__":
    main()