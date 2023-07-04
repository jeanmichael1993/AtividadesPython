maior_valor: int = 0
menor_valor: int = []
numero: int = 0

while numero >= 0:
    numero = int(input('Informe um numero inteiro: '))
    if numero > maior_valor:
        maior_valor = numero
    if numero > 0:
        menor_valor.append(numero)
print(maior_valor)
print(min(menor_valor))