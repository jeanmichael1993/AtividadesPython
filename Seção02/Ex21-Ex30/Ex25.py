import math

a:float = float(input("Entre com o valor de A: "))
b:float = float(input("Entre com o valor de B: "))
c:float = float(input("Entre com o valor de C: "))

if a == 0:
    (print("Não é equação de segundo grau!"))
else:
    D: float = (b**2) - (4 * a * c)
    if D < 0:
        print("Não existe raiz.")
    elif D == 0:
        print("Raiz única!")
        print(f"A raiz é: {(-b) / (2 * a)}")
    elif D > 0:
         x1 = (-b + math.sqrt(D)) / (2 * a)
         x2 = (-b - math.sqrt(D)) / (2 * a)
         print(f"Raiz x1 é : {x1}")
         print(f"Raiz x2 é : {x2}")




