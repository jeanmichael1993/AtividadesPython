def guardar_dados(vetor: float, count: int):
    try:
        for x in range(count):
            vetor.append(float(input(f"Digite o {len(vetor)+1}º numero : ")))
            count -= 1
        vetor.sort()
        return vetor
    except ValueError as error:
        print(f'Valor errado! {error}')
        return guardar_dados(vetor, count)


print(guardar_dados([], count=10))

