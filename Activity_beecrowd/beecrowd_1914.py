
def game():
    name1, play1, name2, play2 = input().split(" ")
    dic: dict = {play1:name1, play2:name2}
    count1, count2 = input().split(" ")
    sum: int = int(count1) + int(count2)
    if sum % 2 == 0:
        print(dic["PAR"])
    else:
        print(dic["IMPAR"])


def main():
    count: int = int(input())
    [game() for i in range(count)]


if __name__ == "__main__":
    main()