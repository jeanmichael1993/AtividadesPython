def fornecer_numero() -> int:
    try:
        numero: int = int(input("Digite um número inteiro positivo: "))
        if numero < 0:
            print("Valor deve ser maior ou igual a zero!")
            fornecer_numero()
        return numero
    except ValueError as error:
        print(f"teve o seguinte erro: {error}, ou seja, o valor não é aceito! ")
        fornecer_numero()


def lista_de_numeros(x: int) -> int:
    lista_numeros: int = []
    valor_de_comparacao: int = 0
    while valor_de_comparacao < x:
        try:
            num: int = int(input("Digite um número inteiro positivo: "))
            if num < 0:
                print(f"Número invalido, inserir valor maior ou igual a 0!")
            else:
                lista_numeros.append(num)
                valor_de_comparacao += 1
        except ValueError as error:
            print(f"O valor inserido não é permitido! {error}")
    return lista_numeros


def formatar_lista(l: int) -> int:
    numero_maior: int = 0
    for x in l:
        if x > numero_maior:
            numero_maior = x
    return numero_maior, l


def imprimir_numero_maior(*args):
    print(f"O maior número é o : {args[0][0]}!")
    cont: int = 0
    for x in args[0][1]:
        if x == args[0][0]:
            cont += 1
    print(f"Ele apareceu {cont} vezes!")


result = formatar_lista(lista_de_numeros(fornecer_numero()))
imprimir_numero_maior(result)
