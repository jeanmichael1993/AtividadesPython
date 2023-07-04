def calcular_area_triangulo():
    while True:
        try:
            base = float(input("Digite a medida da base do triângulo: "))
            altura = float(input("Digite a medida da altura do triângulo: "))
            if base <= 0 or altura <= 0:
                raise ValueError
            area = (base * altura) / 2
            return area
        except ValueError:
            print("Entrada inválida. Certifique-se de digitar valores maiores que zero.")

area_triangulo = calcular_area_triangulo()
print("A área do triângulo é:", area_triangulo)
