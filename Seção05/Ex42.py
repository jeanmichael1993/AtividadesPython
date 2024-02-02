import statistics


def maior_valor(vet: float) -> float:
    media: float = statistics.mean(vet)
    return media


def guarda_valor(n: int, count: int) -> float:
    try:
        vetor: float = []
        for i in range(count, n):
            vetor.append(float(input(f"Digite o {len(vetor)+1}º numero:  ")))
            count +=1
        maior: float = maior_valor(vetor)
        return maior
    except ValueError as error:
        print("Valor errado!")
        return guarda_valor(n , count)


if __name__ == "__main__":
    n: int = int(input("Digite o valor de N: "))
    res: float = guarda_valor(n, count=0)
    print(f'A media dos valores do vetor é : {res}')