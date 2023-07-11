def contar_letras(numero):
    unidades = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
    especiais = ['dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
    dezenas = ['vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
    centenas = ['cem', 'cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos']

    if numero < 10:  # Unidades
        return len(unidades[numero])
    elif numero < 20:  # Números especiais
        return len(especiais[numero - 10])
    elif numero < 100:  # Dezenas
        dezena = dezenas[numero // 10 - 2]
        unidade = unidades[numero % 10]
        return len(dezena) + len(unidade) if numero % 10 != 0 else len(dezena)
    elif numero < 1000:  # Centenas
        centena = centenas[numero // 100]
        resto = numero % 100
        if resto == 0:
            return len(centena)
        else:
            return len(centena) + len('e') + contar_letras(resto)
    elif numero == 1000:  # Mil
        return len('mil')

total_letras = 0

for numero in range(1, 1001):
    total_letras += contar_letras(numero)

print("O total de letras utilizadas de 1 a 1000 é:", total_letras)
