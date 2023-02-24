
contar: int = []
x: int = 1

while len(contar) < 3:
    if x % 3 == 0:
        contar.append(x)
    x += 1


print(contar)

