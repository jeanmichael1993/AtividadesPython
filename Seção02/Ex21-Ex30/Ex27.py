idade: int = int(input("Digite a idade: "))
if idade >= 5 and idade <= 7:
    print("Categoria é Infantil A.")
elif idade >= 8 and idade <= 10:
    print("Categoria é Infantil B.")
elif idade >= 11 and idade <= 13:
    print("Categoria é Juvenil A.")
elif idade >= 14 and idade <= 17:
    print("Categoria é Juvenil B.")
elif idade >= 18:
    print("Categoria é Sênior!")
else:
    print("Idade não pode ser menor que 5!")

