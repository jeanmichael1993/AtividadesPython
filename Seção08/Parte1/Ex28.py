
class Microondas:

    def __init__(self, status):
        self.__status: bool = status

    def show(self):
        """
        :return: return itens information
        """
        print(f'The item is : {"ON" if self.__status == 1 else "OFF"}')

    def on(self):
        self.__status = 1

    def off(self):
        self.__status = 0


def main():
    """
    :return: nome
    """
    item = Microondas(0)
    item.show()


if __name__ == "__main__":
    main()