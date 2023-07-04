import random
tentativas: int = 0
cond: bool = True
valor: int = (random.randint(1, 1000))
while cond:
    print(valor)
    escolha: int = int(input("Digite o valor que você acha que é o aleatório: "))
    tentativas += 1
    if valor == escolha:
        print(f"Parabéns acertou!!!Foram {tentativas} tentativas!!!")

        cond = False
    else:
        print(f"Voçê errou!!! tente novamente! o chute foi maior que o valor!") if escolha > valor else print(f"Voçê errou!!! tente novamente! o chute foi menor que o valor!")