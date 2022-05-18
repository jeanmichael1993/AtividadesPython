switch = {
    1: "Soma de 2 números.",
    2: "Diferença entre 2 números (maior pelo menor)",
    3: "Produto entre 2 números.",
    4: "Divisão entre 2 números (o denominador não pode ser zero)."
}
print("Escolha a opção: ")
for valor in switch:
    print(f"{valor}-{switch[valor]}")

def solicitar_numeros():
    valor_um: float = float(input("Digite o primeiro número: "))
    valor_dois: float = float(input("Digite o segundo número: "))
    return valor_um, valor_dois


opc: int = int(input("Opção: "))
result: str = switch.get(opc, "Opção invalida!")
print(result)
if opc == 1:
    valor_um, valor_dois = solicitar_numeros()
    print(f"A somatoria dos dois números é: {valor_um + valor_dois }")
elif opc == 2:
    valor_um, valor_dois = solicitar_numeros()
    if valor_um > valor_dois:
        resultado: float = valor_um - valor_dois
    else:
        resultado: float = valor_dois - valor_um
    print(f"A Diferença entre os dois números é : {resultado}")
elif opc == 3:
    valor_um, valor_dois = solicitar_numeros()
    print(f"O produto entre os dois números é {(valor_um * valor_dois):.2f}")
elif opc == 4:
    valor_um, valor_dois = solicitar_numeros()
    if valor_dois == 0:
        print("O Denominador não pode ser zero!")
    else:
        print(f"A valor da divisão entre dois números é: {valor_um/valor_dois}")