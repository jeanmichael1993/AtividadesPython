
def to_show(value: int):
    if value == 0:
        print(":)")
    else:
        print(":(")

def weather(a: int, b:int, c:int):
    if a > b and b <= c:
        to_show(0)
    elif a < b and b >= c:
        to_show(1)
    elif a < b and b < c:
        if b-a > c - b:
            to_show(1)
        else:
            to_show(0)
    elif a > b and b > c:
        if b-a < c-b:
            to_show(0)
        else:
            to_show(1)
    elif a == b:
        if b < c:
            to_show(0)
        else:
            to_show(1)



def main():
    a,b,c = input().split(" ")
    a: int = int(a)
    b: int = int(b)
    c: int = int(c)
    weather(a,b,c)



if __name__ == "__main__":
    main()