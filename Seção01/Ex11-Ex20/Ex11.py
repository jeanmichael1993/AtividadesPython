"""
Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em km/h (quilômetros por hora).
A formula de conversão é: K = M * 3.6, sendo K a velocidade em km/h e M em m/s.
"""

velocidade_em_ms = float(input("Digite a velocidade em m/s(metros por segundo)"))
print(f"{velocidade_em_ms * 3.6} km/h")