
valor: float = float(input("Entre com o valor: "))
estado: str = input("Entre com a sigla do estado: ")
estado = estado.upper()


switch = {
    'MG': 0.07,
    'SP': 0.12,
    'RJ': 0.15,
    'MS': 0.08,
}
result = (switch.get(estado, "Number Invalid!"))
if result != "Number Invalid!":
    print(f"{((valor * result) + valor):.2f} será o valor acrescido do imposto!")
else:
    print("Estado invalido!")
