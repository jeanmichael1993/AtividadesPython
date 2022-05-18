

idade: int = int(input("Digite a idade: "))
temp_serv: int = int(input("Digite o tempo de serviço(anos): "))

if idade >= 65 or temp_serv >= 30 or (idade >= 60 and temp_serv >= 25):
    print("Pode aposentar!")
else:
    print("Não pode aposentar!")

