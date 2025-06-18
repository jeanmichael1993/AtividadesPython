
def main():
    a,b = map(float, input().split(" "))
    calculate: float = ((b-a) / a) * 100
    print(f"{calculate:.2f}%")

if __name__ == "__main__":
    main()