"""Leia um temperatura em graus Kelvin e apresente-a convertida em graus Celsius. A fórmula de conversão
é: C = K - 273.15, sendo C a temperatura em Celsius e K a temperatura em Kelvin."""

temperatura_em_graus_kelvin = float(input("Digite a temperatura em graus Kelvin: "))
print(f"A temperatura em Graus Celsius é : { temperatura_em_graus_kelvin - 273.15:.2f}")