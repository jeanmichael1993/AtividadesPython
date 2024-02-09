def concatenar_com_limite(str1, str2, N):
    if N <= 0:
        raise ValueError("N deve ser um valor inteiro positivo")
    resultado = str1 + str2[:N]

    return resultado


if __name__ == "__main__":
    string1: str = input("Digite a primeira frase: ")
    string2: str = input("Digite a segunda frase: ")
    limite: int = int(input("Digite o limite: "))

    resultado_concatenacao_limitada = concatenar_com_limite(string1, string2, limite)
    print("Resultado da concatenação com limite:", resultado_concatenacao_limitada)
