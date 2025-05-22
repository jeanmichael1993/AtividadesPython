def names():
    name, value = input().split(" ")
    name: str = name
    value: int = int(value)
    if name == "Thor":
        print("Y")
    else:
        print("N")



def main():
    cases: int = int(input())
    [names() for i in range(cases)]


if __name__ == "__main__":
    main()