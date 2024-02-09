def tamanho(str, strsize):
    tamanho_str = len(str)
    strsize[0] = tamanho_str


if __name__ == "__main__":
    string: str = input("Digite a frase: ")
    comprimento = [0]
    tamanho(string, comprimento)
    print(f"O comprimento da string é: {comprimento[0]}")
