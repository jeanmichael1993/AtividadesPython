

produtos= {'100': '1.20', '101': '1.30', '102': '1.50', '103': '1.20',
           '104': '1.70', '105': '2.20', '106': '1.00'}


def calcular_quantidade(x: str, quantidade: int):
    valor_produto: float = float(produtos[x])
    valor_total: float = valor_produto * float(quantidade)
    return valor_total


codigo: str = input("Digite o codigo do produto: ")
qtd: int = input("Digite a quantidade do produto: ")
valor_fim = calcular_quantidade(codigo, qtd)
print(f"O valor a pagar é: ${valor_fim:.2f}.")

