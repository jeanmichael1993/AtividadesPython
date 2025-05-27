from datetime import datetime

def main():
    n: int = int(input())
    for i in range(n):
        test: int = int(input())
        year_today = datetime.now().year
        if test >= year_today:
            print(f"{(test+1) - year_today} A.C.")
        else:
            print(f"{year_today - test} D.C.")



if __name__ == "__main__":
    main()