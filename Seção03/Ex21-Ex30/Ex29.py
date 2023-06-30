s: float = 0
for x in range(1, 6):
    resultado: float = 1
    for j in range(1, x*2+1):
        resultado *= j
    s += x/resultado
print(s)
