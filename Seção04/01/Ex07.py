def numero_maior_e_posicao() -> int:
    try:
        numeros: int = []
        for x in range(3):
                numeros.append(int(input("Digite um número: ")))
        maior: int = max(numeros)
        print(f'O maior valor é o : {maior} e ele se encontra na {numeros.index(maior) + 1}ª posição.')
    except ValueError as error:
        print(error)


numero_maior_e_posicao()

