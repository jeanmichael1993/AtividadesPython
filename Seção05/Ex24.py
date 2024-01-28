def gerar_triangulo(n):
    for i in range(n):
        espacos = ' ' * (n - i - 1)
        asteriscos = '*' * (2 * i + 1)
        linha = espacos + asteriscos
        print(linha)

# Exemplo de uso com n=6
gerar_triangulo(6)
