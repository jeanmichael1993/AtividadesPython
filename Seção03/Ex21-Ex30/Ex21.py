def ler_numeros() -> int:
    numeros: int = []
    for x in range(2):
        numeros.append(int(input(f"Digite o {x + 1}º número: ")))
    return numeros

def soma_numero_par_e_impar(x: int) -> int:
    impar: int = 0
    par: int = 0
    for i in range(x[0],x[1] + 1):
        if i % 2 == 0:
            par += i
        else:
            impar *= i
    return impar, par

def imprimir(*args: int):
    print(f"A multiplicação de números impares é {args[0][0]} e a soma de números pares é {args[0][1]}!")

imprimir(soma_numero_par_e_impar(ler_numeros()))