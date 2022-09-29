


def separar_hora_e_minutos(x:str) -> str:
    hora: str = x[0]
    minuto:str = x[1]
    return hora, minuto

def tarifa(x1: str, x2: str) -> float:
    taxa: float = 0
    hora_total_entrada: int = (int(x1[0]) * 60) + int(x1[1])
    hora_total_saida: int = (int(x2[0]) * 60) + int(x2[1])
    if hora_total_saida - hora_total_entrada <= 120:
        taxa = 1.00
    elif hora_total_saida - hora_total_entrada > 120 and hora_total_saida - hora_total_entrada <= 240:
        taxa = 1.40
    else:
        taxa = 2.00
    return taxa

entrada: str = input("Hora e minutos de entrada: ").split(':')
saida: str = input("Hora e minutos de saida: ").split(':')
entrada_separada: str = separar_hora_e_minutos(entrada)
saida_separada: str = separar_hora_e_minutos(saida)
print(f"Valor a pagar é de R${tarifa(entrada_separada,saida_separada):.2f}")