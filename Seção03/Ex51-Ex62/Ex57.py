import math
def obter_valor() -> int:
    try:
        valor_a: int = int(input("Digite o valor de A: "))
        valor_b: int = int(input("Digite o valor de B: "))
        if valor_a > valor_b:
            print("Valor de A deve ser menor que valor de B!!!")
            return obter_valor()
        return valor_a, valor_b
    except ValueError as error:
        print(error)
        return obter_valor()


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


valor_a, valor_b = obter_valor()
primos_ate_100 = obter_primos(valor_b)
cont: int = 0
for x, i in enumerate(primos_ate_100):
    if i >= valor_a:
        cont += 1
        

print(f"Existem {cont} números primos entre {valor_a} e {valor_b}!")