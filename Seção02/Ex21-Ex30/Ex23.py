

ano_bi: int = int(input("Digite o ano: "))
if ano_bi % 400 == 0 or (ano_bi % 4 == 0 and ano_bi % 100 != 0):
    print(f"{ano_bi} é um ano bissexto!")
else:
    print(f"{ano_bi} não é um ano bissexto!")

