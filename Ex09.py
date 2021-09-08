"""
Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin. A fórmula de conversão é:
K = C + 273.15, sendo C a temperatura em Celsius e K a temperatura em Kelvin.
"""

temperatura_em_graus_celsius = float(input("Digite a temperatura em graus Celsius: "))
print(f"A temperadora em graus Kelvin é: {temperatura_em_graus_celsius + 273.15:.2f}")

