vetor: int = []
count: int = 5
codigo: int = None


def ler_numeros(vetor: int, count:int ) -> int:
    try:
        for x in range(count):
            vetor.append(int(input(f"Digite o {len(vetor)+1}º número: ")))
            count -= 1
        return vetor
    except ValueError as error:
        print("Valor digitado está errado!")
        return ler_numeros(vetor, count)


def mostrar_codigo(vetor: int, codigo: int) -> int:
    try:
        while codigo != 0:
            codigo = int(input("Digite os números seguintes para prosseguir : \n(0) fechar o programa \n"
                               "(1) Mostre vetor ordem direta \n"
                               "(2) Mostre vetor ordem inversa: "))
            if 0 < codigo >= 3:
                print("Codigo errado!")
            elif codigo == 1:
                print(vetor)
            elif codigo == 2:
                print(list(reversed(vetor)))
            else:
                pass
    except ValueError as error:
        print("Valor digitador está errado! ")

        mostrar_codigo(vetor, codigo)


mostrar_codigo(ler_numeros(vetor, count), codigo)


