
class Eletrodomestico:

    def __init__(self, ligado):
        self.__ligado = ligado

    def show(self):
        print(f'The item is {"OFF" if self.__ligado == 0 else "ON"}')

    def off(self):
        self.__ligado = 0

    def on(self):
        self.__ligado = 1


def main():
    item = Eletrodomestico(ligado=1)
    item.show()
    item.off()
    item.show()
    item.on()
    item.show()


if __name__ == "__main__":
    main()

