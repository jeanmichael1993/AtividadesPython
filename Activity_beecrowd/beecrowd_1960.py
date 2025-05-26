def main():
    n: int = int(input())
    valores_romanos = [
        (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
        (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
        (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    romano = ""

    for valor, simbolo in valores_romanos:
        while n >= valor:
            romano += simbolo
            n -= valor

    print(romano)

if __name__ == "__main__":
    main()