
class Microondas:

    def __init__(self, status):
        self.__status: bool = status
        self.__closed_door: bool = 0

    def show(self):
        """
        :return: return itens information
        """
        print(f'The item is : {"ON" if self.__status == 1 else "OFF"} ,'
              f'The Door is closed: {"YES" if self.__closed_door == 1 else "NO"}')

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