
class Elevator:


    def __int__(self):
        self.__andar = 0
        self.__total_andar = 0
        self.__cap_elevator = 0
        self.__pessoas = 0

    def inicializa(self, cap_elevator, total_andares):
        self.__cap_elevator = cap_elevator
        self.__total_andar = total_andares
        self.__andar = 0
        self.__pessoas = 0


    def entra(self):
        if self.__cap_elevator > self.__pessoas:
            self.__pessoas += 1
            return print(f"Tem {self.__pessoas} no elevador.")

    def sai(self):
        if self.__pessoas > 0:
            self.__pessoas -= 1
            return print(f"Tem {self.__pessoas} no elevador.")

    def sobe(self):
        if self.__andar < self.__total_andar:
            self.__andar += 1
            return print(f"Andar atual: {self.__andar}")

    def desce(self):
        if self.__andar >= 1:
            self.__andar -= 1
            return print(f"Andar atual: {self.__andar}")


def main():
    elevator = Elevator()
    elevator.inicializa(10, 5)
    elevator.sobe()
    elevator.sobe()
    elevator.entra()
    elevator.entra()
    elevator.sai()
    elevator.sai()
    elevator.sai()
    elevator.desce()
    elevator.desce()
    elevator.desce()


if __name__ == "__main__":
    main()


