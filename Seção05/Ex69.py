def encontrar_mdc(a, b):
    # Encontra o MDC (máximo divisor comum) usando o algoritmo de Euclides
    while b:
        a, b = b, a % b
    return a


def simplificar_fracao(frac):
    # Encontra o MDC entre o numerador e o denominador
    mdc = encontrar_mdc(frac[0], frac[1])

    # Simplifica a fração dividindo o numerador e o denominador pelo MDC
    frac[0] //= mdc
    frac[1] //= mdc


def somar_fracoes(frac1, frac2):
    # Soma as frações
    resultado = [frac1[0] * frac2[1] + frac2[0] * frac1[1], frac1[1] * frac2[1]]
    simplificar_fracao(resultado)
    return resultado


def subtrair_fracoes(frac1, frac2):
    # Subtrai as frações
    resultado = [frac1[0] * frac2[1] - frac2[0] * frac1[1], frac1[1] * frac2[1]]
    simplificar_fracao(resultado)
    return resultado


def multiplicar_fracoes(frac1, frac2):
    # Multiplica as frações
    resultado = [frac1[0] * frac2[0], frac1[1] * frac2[1]]
    simplificar_fracao(resultado)
    return resultado


def dividir_fracoes(frac1, frac2):
    # Divide as frações
    resultado = [frac1[0] * frac2[1], frac1[1] * frac2[0]]
    simplificar_fracao(resultado)
    return resultado


# Função principal
def main():
    # Leitura das frações
    numerador1 = int(input("Digite o numerador da primeira fração: "))
    denominador1 = int(input("Digite o denominador da primeira fração: "))
    numerador2 = int(input("Digite o numerador da segunda fração: "))
    denominador2 = int(input("Digite o denominador da segunda fração: "))

    # Criação das frações
    fracao1 = [numerador1, denominador1]
    fracao2 = [numerador2, denominador2]

    # Simplifica as frações
    simplificar_fracao(fracao1)
    simplificar_fracao(fracao2)

    # Operações com as frações
    resultado_soma = somar_fracoes(fracao1, fracao2)
    resultado_subtracao = subtrair_fracoes(fracao1, fracao2)
    resultado_multiplicacao = multiplicar_fracoes(fracao1, fracao2)
    resultado_divisao = dividir_fracoes(fracao1, fracao2)

    # Apresenta os resultados
    print("\nResultados:")
    print("Soma:", resultado_soma[0], "/", resultado_soma[1])
    print("Subtração:", resultado_subtracao[0], "/", resultado_subtracao[1])
    print("Multiplicação:", resultado_multiplicacao[0], "/", resultado_multiplicacao[1])
    print("Divisão:", resultado_divisao[0], "/", resultado_divisao[1])


if __name__ == "__main__":
    main()
