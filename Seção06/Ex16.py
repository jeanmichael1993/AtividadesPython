def converter_para_binario_e_gravar_arquivo(vetor_numeros, nome_arquivo_saida):
    with open(nome_arquivo_saida, 'w+') as arquivo:
        for numero in vetor_numeros:
            binario = bin(numero)[2:]  # Converte o n�mero para bin�rio e remove o prefixo '0b'
            arquivo.write(binario + '\n')

# Exemplo de uso
numeros = [23, 45, 12, 8, 17, 6, 33, 51, 9, 21]
arquivo_saida = 'binarios.txt'

converter_para_binario_e_gravar_arquivo(numeros, arquivo_saida)