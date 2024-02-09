
if __name__ == "__main__":
    try:
        substring: str = str(input("Digite uma substring:"))
        string: str = str(input("Digite o texto:"))
        print(f'A substring está na posição: {string.find(substring) if string.find(substring) != -1 else -1}')
    except ValueError as error:
        print('valor errado!')