def ler_arquivo_entrada(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        linhas, colunas, quantidade_anuladas = map(int, arquivo.readline().split())
        posicoes_anuladas = [tuple(map(int, arquivo.readline().split())) for _ in range(quantidade_anuladas)]
    return linhas, colunas, posicoes_anuladas

def gerar_matriz(linhas, colunas, posicoes_anuladas):
    matriz = [[1] * colunas for _ in range(linhas)]

    for linha, coluna in posicoes_anuladas:
        matriz[linha - 1][coluna - 1] = 0

    return matriz

def gravar_matriz_em_arquivo(nome_arquivo_saida, matriz):
    with open(nome_arquivo_saida, 'w') as arquivo:
        for linha in matriz:
            linha_str = ' '.join(map(str, linha))
            arquivo.write(f"{linha_str}\n")

# Exemplo de uso
arquivo_entrada = 'Ex17Arq.txt'
arquivo_saida = 'saidaEx17q.txt'

linhas, colunas, posicoes_anuladas = ler_arquivo_entrada(arquivo_entrada)
matriz_resultante = gerar_matriz(linhas, colunas, posicoes_anuladas)
gravar_matriz_em_arquivo(arquivo_saida, matriz_resultante)
