def ler_string_teclado(vetor, tamanho_maximo):
    i = 0
    while i < tamanho_maximo:
        caractere = input("Digite um caractere (ou pressione Enter para encerrar): ")
        if not caractere or i == tamanho_maximo:
            break
        vetor[i] = caractere
        i += 1


if __name__ == "__main__":
    tamanho_maximo = 10
    vetor_caracteres = [''] * tamanho_maximo
    ler_string_teclado(vetor_caracteres, tamanho_maximo)
    print("Vetor de caracteres lido:", vetor_caracteres)
