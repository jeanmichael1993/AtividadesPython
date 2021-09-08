""" Leia uma temperatura em graus Fahrenheit e apresente-a convertida em grau Celsius.
A fórmula de conversão é: C = 5.0 * (F - 32.0)/9.0, sendo C a temperatura em Celsius e F a temperatura em Fahrenheit.
"""

graus_fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
print(f"A temperatura é em grau Celsius: {(5.0 * (graus_fahrenheit - 32.0)/9.0):.2f}")
