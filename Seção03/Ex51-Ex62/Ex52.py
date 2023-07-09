saque: float = float(input("Digite o valor do saque:  "))
nota_100: int = 0
nota_50: int = 0
nota_20: int = 0
nota_10: int = 0
nota_5: int = 0
nota_2: int = 0
nota_1: int = 0
while saque > 0:
    if saque >= 100:
        saque -= 100
        nota_100 += 1
    elif saque >= 50:
        saque -= 50
        nota_50 += 1
    elif saque >= 20:
        saque -= 20
        nota_20 +=1
    elif saque >= 10:
        saque -= 10
        nota_10 += 1
    elif saque >= 5:
        saque -= 5
        nota_5 += 1
    elif saque >= 2:
        saque -= 2
        nota_2 += 1
    elif saque >= 1:
        saque -= 1
        nota_1 += 1


teste: int = {'100': nota_100, '50': nota_50, '20': nota_20, '10': nota_10, '5': nota_5, '2': nota_2, '1': nota_1}


for keys, valor in teste.items():
    if keys == '1' and valor > 0:
            print(f'Serão {valor} quantidade(s) de ${keys} real')
    elif valor > 0:
        print(f'Serão {valor} quantidade(s) de ${keys} reais')

