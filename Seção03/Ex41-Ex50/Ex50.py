altura_chico = 1.50
crescimento_chico = 0.02

altura_ze = 1.10
crescimento_ze = 0.03

anos = 0

while altura_ze <= altura_chico:
    altura_chico += crescimento_chico
    altura_ze += crescimento_ze
    anos += 1

print("Serão necessários", anos, "anos para que Zé seja maior que Chico.")
