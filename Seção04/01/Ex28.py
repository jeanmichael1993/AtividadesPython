vetor: int = []
count: int = 10

for x in range(count):
    vetor.append(int(input("Digite o valor: ")))

v1: int = [numero for numero in vetor if numero % 2]
v2: int = [numero for numero in vetor if not numero % 2]

print(v1)
print(v2)