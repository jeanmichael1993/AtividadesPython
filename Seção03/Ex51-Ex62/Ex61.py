def is_palindrome(num):
    # Converte o número em uma string e verifica se ela é igual à sua inversa
    return str(num) == str(num)[::-1]

maior_palindromo = 0

for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        produto = i * j
        if produto > maior_palindromo and is_palindrome(produto):
            maior_palindromo = produto

print("O maior palíndromo feito a partir do produto de dois números de 3 dígitos é:", maior_palindromo)
