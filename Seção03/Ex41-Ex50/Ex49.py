def calcular_meses_igualdade(salario_carlos, taxa_carlos, salario_joao, taxa_joao):
    meses = 0

    while salario_joao <= salario_carlos:
        salario_carlos += salario_carlos * (taxa_carlos / 100)
        salario_joao += salario_joao * (taxa_joao / 100)
        meses += 1

    return meses

salario_carlos = float(input("Digite o salário de Carlos: "))
taxa_carlos = float(input("Digite a taxa de rendimento de Carlos (%): "))
salario_joao = salario_carlos / 3
taxa_joao = float(input("Digite a taxa de rendimento de João (%): "))

meses = calcular_meses_igualdade(salario_carlos, taxa_carlos, salario_joao, taxa_joao)

print("Levará", meses, "meses para que o valor pertencente a João iguale ou ultrapasse o valor pertencente a Carlos.")
