
limit: int = 100

for x in range(1, limit+1):
    print(x)

x2: int = 1
while x2 < limit + 1:
    print(x2)
    x2 += 1

validacao: int = 100
number: int = 1
while True:
    if number > validacao:
        break
    else:
        print(number)
        number += 1
