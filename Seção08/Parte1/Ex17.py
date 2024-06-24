
class Eletrodomestico:

    def __init__(self):
        self.__ligado = 1

    def show(self):
        print(f'The item is {"OFF" if self.__ligado == 0 else "ON"}')

def main():
    item = Eletrodomestico()
    item.show()


if __name__ == "__main__":
    main()

