def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(map(str, linha)))

def verificar_vitoria(tabuleiro, jogador):
    # Verifica linhas e colunas
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)) or all(tabuleiro[j][i] == jogador for j in range(3)):
            return True

    # Verifica diagonais
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True

    return False

def obter_proxima_jogada(tabuleiro, jogador):
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == 0:
                # Faça a jogada e verifique se é uma jogada vitoriosa
                tabuleiro[i][j] = jogador
                if verificar_vitoria(tabuleiro, jogador):
                    tabuleiro[i][j] = 0  # Desfaz a jogada se for vitoriosa
                    return i, j
                tabuleiro[i][j] = 0  # Desfaz a jogada

    # Se não houver jogada vitoriosa, jogue em qualquer posição vazia
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == 0:
                return i, j

    return None

# Exemplo de uso
tabuleiro = [[-1, 1, 1],
             [-1, -1, -1],
             [0, 1, 0]]

print("Tabuleiro atual:")
imprimir_tabuleiro(tabuleiro)

jogador_atual = -1  # Supondo que você é o jogador representado por -1

proxima_jogada = obter_proxima_jogada(tabuleiro, jogador_atual)

if proxima_jogada:
    print(f"Próxima jogada em ({proxima_jogada[0]}, {proxima_jogada[1]})")
else:
    print("O jogo terminou ou está empatado.")
