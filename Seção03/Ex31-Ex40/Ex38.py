def encontrar_terno_pitagorico():
    for a in range(1, 1000):
        for b in range(a + 1, 1000):
            c = 1000 - a - b
            if c > 0 and (a**2 + b**2 == c**2):
                return a, b, c

a, b, c = encontrar_terno_pitagorico()
print("Terno pitagórico encontrado:")
print("a =", a)
print("b =", b)
print("c =", c)
print("Soma (a + b + c) =", a + b + c)