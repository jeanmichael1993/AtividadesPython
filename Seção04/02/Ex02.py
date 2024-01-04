matriz: int = [[i * 0 for i in range(5)] for j in range(5)]
count: int = 0
for x in matriz:
    x[count] = 1
    count += 1

for x in matriz:
    print(x)