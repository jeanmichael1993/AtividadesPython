valor: int = 1
soma: int = 0
soma2: int = 0
for i in range(1, 100+1):
    soma+= i**2

for i in range(1, 100+1):
    soma2+= i

print((soma2**2) - soma)
