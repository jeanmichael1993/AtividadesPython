def maiusculo(caractere):
    # Verifica se o argumento é um caractere
    if len(caractere) != 1:
        raise ValueError("O argumento deve ser um único caractere")
    caractere_maiusculo = caractere.upper()

    return caractere_maiusculo


if __name__ == "__main__":
    caractere: str = input("Digite o caractere: ")
    resultado_maiusculo = maiusculo(caractere)
    print(f"O caractere {caractere} em maiúsculo é: {resultado_maiusculo}")
