def test_sum():
    attempts: int = int(input())
    soma: int = 0
    for i in range(1, attempts +1 ):
        if i % 2 != 0:
            soma +=1
        else:
            soma -=1
    print(soma)


def main():
    cases: int = int(input())
    [test_sum() for i in range(cases)]


if __name__ == "__main__":
    main()