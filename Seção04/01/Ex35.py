
def soma(vet1: int, vet2: int):
    soma: int = 0
    soma_vetor: int = []
    resto: int = 0
    for i, j in zip(vet1, vet2):
        soma = i + j + resto
        if soma >= 10:
            soma_vetor.append(soma - 10)
            resto = 1
        else:
            soma_vetor.append(soma)
            resto = 0
    return print(soma_vetor)


num_a: int = int(input("Digite o Valor de A: "))
num_b: int = int(input("Digite o Valor de B: "))
vetor_a: int = [int(a) for a in str(num_a)]
vetor_b: int = [int(a) for a in str(num_b)]
soma(vetor_a, vetor_b)

