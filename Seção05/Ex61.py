def sao_anagramas(str1, str2):
    # Remove espaços em branco e converte para minúsculas para evitar diferenças de caso
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Verifica se as strings têm o mesmo conjunto de caracteres
    return sorted(str1) == sorted(str2)


if __name__ == "__main__":
    string1: str = input("Digite a palavra 1:")
    string2: str = input("Digite a palavra 2: ")

    resultado = sao_anagramas(string1, string2)
    print(f"As strings '{string1}' e '{string2}' são anagramas: {resultado}")
