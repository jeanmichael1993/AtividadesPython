

def pode_formar_triangulo(x, y, z):
    return x + y > z and x + z > y and y + z > x

def main():
    A,B,C,D = map(int, input().split(" "))

    if (
            pode_formar_triangulo(A, B, C) or
            pode_formar_triangulo(A, B, D) or
            pode_formar_triangulo(A, C, D) or
            pode_formar_triangulo(B, C, D)
    ):
        print('S')
    else:
        print('N')


if __name__ == "__main__":
    main()