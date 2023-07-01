def calcular_mmc(numeros):
    mmc = 1
    fator = 2
    while numeros:
        divisivel = False
        for i in range(len(numeros)):
            if numeros[i] % fator == 0:
                divisivel = True
                print(numeros[i], fator)
                numeros[i] //= fator

        if divisivel:
            mmc *= fator
        else:
            fator += 1
        if fator > max(numeros):
            break
    for num in numeros:
        mmc *= num
    return mmc

numeros = list(range(1, 21))
resultado = calcular_mmc(numeros)
print(resultado)