def guardar_valores(vetor:int, count: int) -> int:
    try:
        for x in range(count):
            vetor.append(int(input(f"Digite o {len(vetor)+1}º número: ")))
            count -= 1
        return vetor
    except ValueError as error:
        print(f"Valor digitado incorretamente! {error}")
        return guardar_valores(vetor, count)


vet: int = guardar_valores([], count=10)
vet.sort()
print(vet)

