
class Microondas:

    def __init__(self):
        self.__on: bool = 0

    def show(self):
        """
        :return: return itens information
        """
        print(f'The item is : {"ON" if self.__on == 1 else "OFF"}')


def main():
    """
    :return: nome
    """
    item = Microondas()
    item.show()


if __name__ == "__main__":
    main()