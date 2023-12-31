vetor_1: int = []
vetor_2: int = []
count: int = 10
for x in range(count):
    vetor_1.append(int(input(f"{len(vetor_1) + 1}: ")))
for x in range(count):
    vetor_2.append(int(input(f"{len(vetor_2)+1}: ")))
vetor_c: int = [x - j for x, j in zip(vetor_1, vetor_2)]
print(vetor_c)

