def reajuste_salarial(salario_atual: float, tempo_servico: int) -> float:
    bonus: float = calculo_bonus(tempo_servico)
    if salario_atual <= 500:
        return calculo_salarial(salario_atual, bonus, 0.25)
    elif salario_atual > 500 and salario_atual <= 1000:
        return calculo_salarial(salario_atual,  bonus, 0.20)
    elif salario_atual > 1000 and salario_atual <= 1500:
        return calculo_salarial(salario_atual, bonus, 0.15)
    elif salario_atual > 1500 and salario_atual <= 2000:
        return calculo_salarial(salario_atual,  bonus, 0.10)
    else:
        return calculo_salarial(salario_atual, bonus)


def calculo_salarial(salario_atual: float, bonus: float, taxa: float = 0) -> float:
    return ((salario_atual * taxa) + salario_atual) + bonus


def calculo_bonus(tempo_servico: int) -> float:
    if tempo_servico < 1:
        return 0
    elif tempo_servico >= 1 and tempo_servico <= 3:
        return 100
    elif tempo_servico >= 4 and tempo_servico <= 6:
        return 200
    elif tempo_servico >= 7 and tempo_servico <= 10:
        return 300
    elif tempo_servico > 10:
        return 500


def mostrar_novo_salario(novo_salario: float):
    print(novo_salario)


salario_atual: float = float(input("Digite o salario atual: "))
tempo_servico: int = int(input("Digite o tempo de seviço(Anos): "))
mostrar_novo_salario(reajuste_salarial(salario_atual, tempo_servico))

