def maior_valor(vet: int) -> int:
    maior: int = 0
    for i in vet:
        if i > maior:
            maior = i
    return maior


def guarda_valor(n: int, count: int) -> int:
    try:
        vetor: int = []
        for i in range(count, n):
            vetor.append(int(input(f"Digite o {len(vetor)+1}º numero:  ")))
            count +=1
        maior: int = maior_valor(vetor)
        return maior
    except ValueError as error:
        print("Valor errado!")
        return guarda_valor(n , count)


if __name__ == "__main__":
    n: int = int(input("Digite o valor de N: "))
    res: int = guarda_valor(n, count=0)
    print(f'O maior valor do vetor é : {res}')