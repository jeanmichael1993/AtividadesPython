valor_usado: int = 0
qtd_numeros_lidos: int = 0
qtd_numeros_pares: int = 0
while valor_usado != 1000:
    try:
        valor_usado = int(input("Digite um número inteiro: "))
        if valor_usado % 2 == 0:
            print(f"O valor usado {valor_usado} é par!")
            qtd_numeros_pares += 1
        else:
            print(f"O valor usado {valor_usado} não é par!")
        qtd_numeros_lidos += 1
    except ValueError as error:
        print(f"Valor digitado é diferente do solicitado! {error}")
print(f"A quantidade de números pares são: {qtd_numeros_pares}")
print(f"A quantidade de números utilizados são: {qtd_numeros_lidos}")

