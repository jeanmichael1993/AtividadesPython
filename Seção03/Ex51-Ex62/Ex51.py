porcentagem: float = 0.015
salario_base: float = 2030
ano_contratado: int = 1996
dobro: float = 30

while ano_contratado < 2023:
    dobro += (dobro * 2)
    salario_base += dobro
    print(salario_base)
    ano_contratado += 1