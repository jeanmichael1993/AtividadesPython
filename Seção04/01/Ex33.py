vetor: int = []
count: int = 4
for x in range(count):
    vetor.append(int(input("Digite o valor : ")))
vetor.sort(reverse=True)
try:
    while vetor.index(0) >= 0:
        vetor.remove(0)
except ValueError:
    pass
print(vetor)
