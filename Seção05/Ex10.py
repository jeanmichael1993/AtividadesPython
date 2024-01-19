def num_maior(num_a: int, num_b: int) -> int:
    if num_a > num_b:
        return num_a
    else:
        return num_b

def guardar_dados() -> int:
    num_a: int = int(input("Digite o valor de A: "))
    num_b: int = int(input("Digite o valor de B: "))
    return num_a, num_b


if __name__ == '__main__':
    num_a, num_b = guardar_dados()
    print(f'o valor maior entre A e B é o : {num_maior(num_a, num_b)}')

