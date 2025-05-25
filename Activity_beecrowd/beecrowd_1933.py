
def main():
    a,b =  map(int, input().split(" "))
    list: int = [a, b]
    list.sort()
    print(list[1])

if __name__ == "__main__":
    main()