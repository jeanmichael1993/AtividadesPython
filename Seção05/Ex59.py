

def criar_vetor(n: int, cod: int) -> int:
    try:
        vet: int = set({})
        for i in range(n):
            vet.add(int(input(f"Digite um valor do vetor {cod}: ")))
        return vet
    except ValueError as error:
        print('Valor errado!')


if __name__ == "__main__":
    try:
        n: int = int(input("Digite o número de elementos: "))
        vet1: int = criar_vetor(n, cod=1)
        vet2: int = criar_vetor(n, cod=2)
        print(vet1)
        print(vet2)
        print(f'união {vet1.union(vet2)}')
    except ValueError as error:
        print('Valor errado!')