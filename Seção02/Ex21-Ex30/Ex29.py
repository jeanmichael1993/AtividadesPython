import random

acertos: int = 0
for x in range(1,6):
    valor_um: int = random.randrange(1, 100)
    valor_dois: int = random.randrange(1, 100)
    print(f"Qual a soma de {valor_um} + {valor_dois}?")
    resposta: int = int(input("Resposta:"))
    if valor_um + valor_dois == resposta:
        print(f"Resposta correta, {valor_um} + {valor_dois} é igual a {resposta}!")
        acertos = acertos + 1
    else:
        print(f"Você errou, a resposta correta é : {valor_um} + {valor_dois} = {valor_um+valor_dois}")

print(f"O(A) aluno(a) acertou {acertos} vezes!")