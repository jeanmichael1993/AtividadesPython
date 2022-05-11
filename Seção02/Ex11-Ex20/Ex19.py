
value: int = int(input("Write a number integer: "))

if value % 3 == 0 or value % 5 == 0:
    if value % 3 == 0 and value % 5 == 0:
        pass
    else:
        print(f"{value} é divisivel por 3 ou 5 mas não simultaneamente pelos dois.")