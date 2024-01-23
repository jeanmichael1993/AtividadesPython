def forma_triangulo(lado1, lado2, lado3):
    return (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1)

def tipo_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 and lado2 == lado3:
        return "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return "Isósceles"
    else:
        return "Escaleno"

def main():
    # Recebe três valores do usuário
    lado1 = float(input("Digite o comprimento do primeiro lado: "))
    lado2 = float(input("Digite o comprimento do segundo lado: "))
    lado3 = float(input("Digite o comprimento do terceiro lado: "))

    # Verifica se os lados formam um triângulo
    if forma_triangulo(lado1, lado2, lado3):
        print("Os lados formam um triângulo.")

        # Determina e mostra o tipo de triângulo
        tipo = tipo_triangulo(lado1, lado2, lado3)
        print("O triângulo é do tipo:", tipo)
    else:
        print("Os lados não formam um triângulo.")

if __name__ == "__main__":
    main()
