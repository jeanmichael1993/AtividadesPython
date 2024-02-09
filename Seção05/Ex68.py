def intercalar_strings(str1, str2):
    len_str1, len_str2 = len(str1), len(str2)
    tamanho_maior = max(len_str1, len_str2)
    str1 = str1.ljust(tamanho_maior)
    str2 = str2.ljust(tamanho_maior)
    resultado_intercalado = ''.join(a + b for a, b in zip(str1, str2))
    str1 = resultado_intercalado


if __name__ == "__main__":
    string1: str = input("Digite a primeira palavra: ")
    string2: str = input("Digite a segunda palavra: ")
    intercalar_strings(string1, string2)
    print("String intercalada:", string1)
