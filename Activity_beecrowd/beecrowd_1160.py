import math


def main():
    try:
        casos_teste = int(input())
        for _ in range(casos_teste):
            years = 0
            pa, pb, g1, g2 = input().split(" ")
            pa = int(pa)
            pb = int(pb)
            g1 = float(g1)
            g2 = float(g2)
            while pa <= pb:
                pa = pa + (pa * (g1/100))
                pa = math.floor(pa)
                pb = pb + (pb * (g2 / 100))
                if pb == float('inf'):
                    break
                pb = math.floor(pb)
                years += 1
            if years > 100:
                print("Mais de 1 seculo.")
            else:
                print(f"{years} anos.")

    except TypeError:
        print("Must be a number integer.")
        main()


if __name__ == "__main__":
    main()


