
class Eletrodomestico:

    def __init__(self, ligado):
        self.__ligado = ligado

    def show(self):
        print(f'The item is {"OFF" if self.__ligado == 0 else "ON"}')

def main():
    item = Eletrodomestico(ligado=1)
    item.show()


if __name__ == "__main__":
    main()

