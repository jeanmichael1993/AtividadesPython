def converter_km_para_ms(velocidade_km):
    return velocidade_km / 3.6

def converter_ms_para_km(velocidade_ms):
    return velocidade_ms * 3.6

while True:
    print("MENU DE CONVERSÃO DE VELOCIDADES:")
    print("1. Converter de km/h para m/s")
    print("2. Converter de m/s para km/h")
    print("3. Finalizar o programa")

    opcao = input("Escolha uma opção (1, 2 ou 3): ")

    if opcao == "1":
        velocidade_km = float(input("Digite a velocidade em km/h: "))
        velocidade_ms = converter_km_para_ms(velocidade_km)
        print("Velocidade em m/s:", velocidade_ms)
        print()
    elif opcao == "2":
        velocidade_ms = float(input("Digite a velocidade em m/s: "))
        velocidade_km = converter_ms_para_km(velocidade_ms)
        print("Velocidade em km/h:", velocidade_km)
        print()
    elif opcao == "3":
        print("Programa finalizado.")
        break
    else:
        print("Opção inválida. Digite 1, 2 ou 3.")
        print()
