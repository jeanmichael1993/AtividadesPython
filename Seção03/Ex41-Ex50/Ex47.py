def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

while True:
    print("MENU DE OPÇÕES:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Saída")

    opcao = input("Escolha uma opção (1, 2, 3, 4 ou 5): ")

    if opcao == "5":
        print("Programa finalizado.")
        break

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == "1":
            resultado = adicao(num1, num2)
            print("Resultado da adição:", resultado)
        elif opcao == "2":
            resultado = subtracao(num1, num2)
            print("Resultado da subtração:", resultado)
        elif opcao == "3":
            resultado = multiplicacao(num1, num2)
            print("Resultado da multiplicação:", resultado)
        elif opcao == "4":
            if num2 == 0:
                print("Divisão por zero não é permitida.")
            else:
                resultado = divisao(num1, num2)
                print("Resultado da divisão:", resultado)
        else:
            print("Opção inválida. Digite 1, 2, 3, 4 ou 5.")

        print()
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números válidos.")
        print()
