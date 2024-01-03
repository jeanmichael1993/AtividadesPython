def guardar_dados(vetor: int, count: int) -> int:
    try:
        for x in range(count):
            vetor.append(int(input(f"Digite o {len(vetor)+1}º número: ")))
            count -= 1
        return vetor
    except ValueError as error:
        print(f'Valor inserido está errado!!!{error}')
        return guardar_dados(vetor, count)


vet1: int = guardar_dados([], count=6)
vet2: int = guardar_dados([], count=5)
vet1.sort()
vet2.sort(reverse=True)
print(vet1+vet2)
