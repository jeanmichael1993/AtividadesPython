s: float = 0.0
lista1: int = []
lista2: int = []
for i in range(1, 100, 2):
    lista1.append(i)

for x in range(1, 50+1):
    lista2.append(x)

for t in range(50):
    s += int(lista1[t]) / int(lista2[t])
    print(s)

