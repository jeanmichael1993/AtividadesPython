
def calculate(x: int,p: int, n:int):
    result: bool = []
    for i in range(n-1):
        if i != n-1:
            if x[i + 1] - x[i] < p:
                result.append(True)
            else:
                result.append(False)
    if False in result:
        print("GAME OVER")
    else:
        print("YOU WIN")



def main():
    p, n = map(int, input().split(" "))
    listt = list(map(int, input().split()))
    calculate(listt,p,n)

if __name__ == "__main__":
    main()