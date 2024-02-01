
def cont_pares(vet: int) -> int:
    soma: int = 0
    for i in vet:
        if i % 2 == 0:
            soma += 1
    return soma


if __name__ == "__main__":
    vet: int = [1, 4, 5, 11, 10, 4, 5]
    resultado: int = cont_pares(vet)
    print(f'O vetor tem a seguinte quantidade de pares: {resultado}')