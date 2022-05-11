

a: float = float(input("Escreva o valor de A: "))
b: float = float(input("Escreva o valor de B: "))
c: float = float(input("Escreva o valor de C: "))

if a < b + c and b < c + a and c < a + b:
    if a == b == c:
        print(f"Triângulo Equilátero")
    if a == b != c or c == b != a or c == a != b:
        print(f"Triângulo Isósceles")
    if a != b != c:
        print(f"Triângulo Escaleno")
