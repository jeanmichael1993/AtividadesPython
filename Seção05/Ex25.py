def calcular_serie(n):
    s = 0
    for i in range(1, n + 1):
        numerador = i**2 + 1
        denominador = i + 3
        termo = numerador / denominador
        s += termo
    return s

# Exemplo de uso com N=5
resultado = calcular_serie(5)
print(resultado)
