import math

def obter_primos(n):
    # Cria um array com todos os elementos inicializados como True
    primos = [True] * (n+1)
    primos[0] = primos[1] = False


    # O loop percorre os números até a raiz quadrada de n
    for p in range(2, int(math.sqrt(n)) + 1):
        if primos[p] == True:
            # Marca como False todos os múltiplos de p
            for i in range(p * p, n+1, p):
                primos[i] = False


    # Retorna uma lista com os números primos
    lista_primos = [x for x in range(n+1) if primos[x]]
    return lista_primos


valor: int = int(input("Digite um número inteiro não negativo: "))
primos_ate_100 = obter_primos(valor)
print(f'{valor} é primo!') if primos_ate_100.count(valor) else print(f'{valor} não é primo!')