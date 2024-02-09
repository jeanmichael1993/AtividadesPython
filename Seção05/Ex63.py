def comparar_strings(str1, str2) -> bool:
    return str1 == str2


if __name__ == "__main__":
    string1: str = input("Digite a primeira palavra: ")
    string2: str = input("Digite a segunda palavra: ")
    resultado = comparar_strings(string1, string2)

    if resultado:
        print("As strings são iguais.")
    else:
        print("As strings são diferentes.")
