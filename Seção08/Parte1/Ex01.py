
class Person:

    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def show(self) -> str:
        return print(f"Name: {self.__name}, Address: {self.__address}, Phone: {self.__phone}")


def main():
    pessoa = Person('Jean', 'Teste2', '2323242232')
    pessoa.show()


if __name__ == "__main__":
    main()



