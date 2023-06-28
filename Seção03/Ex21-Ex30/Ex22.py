
def digitar_numero() -> int:
    numero = 10
    lista_numeros: int = []
    while 10 <= numero <= 20:
        try:
            numero: int = int(input("Digite um número inteiro entre 10 a 20: "))
            if numero < 10 or numero > 20:
                print(f"numero {numero} fora do padrão!")
            elif str(numero).isdigit():
                print(numero)
                lista_numeros.append(numero)
            print(lista_numeros)
        except ValueError as error:
            print(f"Número digitado está incorreto: {error}")
            continue
    return lista_numeros


def imprimir_media(x: int):
    print(x)
    media = sum(x) / len(x)
    print(f"A média é : {media}")


imprimir_media(digitar_numero())