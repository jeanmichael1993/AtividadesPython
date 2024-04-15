
class Person:

    def __init__(self):
        self.__name = 'Jean'
        self.__address = 'teste2'
        self.__phone = '232322424'

    def show(self) -> str:
        return print(f"Name: {self.__name}, Address: {self.__address}, Phone: {self.__phone}")


def main():
    pessoa = Person()
    pessoa.show()


if __name__ == "__main__":
    main()



