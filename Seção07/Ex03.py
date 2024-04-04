pessoas: str = [['jean',18,1.80],['teste1',20, 1.75],['teste2',20,1.79],['teste3', 30, 1.67]]

for i in pessoas:
    if i[0].upper() == 'JEAN':
        del pessoas[pessoas.index(i)]

print(pessoas)