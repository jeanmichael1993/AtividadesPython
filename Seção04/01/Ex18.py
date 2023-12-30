vetor: int = []
count: int = 10
multiplos: int = []


def guardar_vetor(vetor: int, count: int) -> int:
    try:
        for x in range(count):
            vetor.append(int(input(f'Digite o {len(vetor) + 1}º número: ')))
            count -= 1
        return vetor
    except ValueError as error:
        print("Valor digitado está incorreto!")
        return guardar_vetor(vetor, count)


def quardar_x() -> int:
    x: int = None
    try:
        x = int(input("Digite um valor para x: "))
        if x <= 0:
            print("Valor digitado não aceito!")
            return quardar_x()
        else:
            return x
    except ValueError as error:
        print("Valor digitado está errado! ")
        return quardar_x()


def mostrar_multiplos(vetor: int, x: int, multiplos: int):
    for j in vetor:
        if j % x == 0:
            multiplos.append(j)
        else:
            pass
    print(f'O(s) numero(s) multiplos de {x} são :{multiplos}')


mostrar_multiplos(guardar_vetor(vetor, count), quardar_x() , multiplos)
