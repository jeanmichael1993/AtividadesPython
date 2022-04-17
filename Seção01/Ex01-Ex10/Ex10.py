"""
Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida em m/s(metros por segundo). A fórmula
de conversão é: M = K/3.6, sendo K a velocidade em km/h e M em m/s.

"""

velocidade_kmh = float(input("Digite a velocidade em km/h: "))
print(f"{velocidade_kmh/3.6:.2f} m/s")

