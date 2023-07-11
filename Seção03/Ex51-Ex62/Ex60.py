numeros = []
soma = 0
quantidade = 0
maior = float('-inf')
menor = float('inf')
soma_pares = 0
quantidade_pares = 0

while True:
    numero = int(input("Digite um número (0 para sair): "))
    if numero == 0:
        break

    numeros.append(numero)
    soma += numero
    quantidade += 1

    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

    if numero % 2 == 0:
        soma_pares += numero
        quantidade_pares += 1

media = soma / quantidade
media_pares = soma_pares / quantidade_pares

print("Soma dos números digitados:", soma)
print("Quantidade de números digitados:", quantidade)
print("Média dos números digitados:", media)
print("Maior número digitado:", maior)
print("Menor número digitado:", menor)
print("Média dos números pares:", media_pares)
