

def game_rules(case: int, p1: str , p2: str) -> str:
    if (p1 == "tesoura" and p2 == "papel"
    or p1 == "papel" and p2 == "pedra"
    or p1 == "pedra" and p2 == "lagarto"
    or p1 == "lagarto" and p2 == "Spock"
    or p1 =="Spock" and p2 == "tesoura"
    or p1 == "tesoura" and p2 == "lagarto"
    or p1 == "lagarto" and p2 == "papel"
    or p1 == "papel" and p2 == "Spock"
    or p1 == "Spock" and p2 == "pedra"
    or p1 == "pedra" and p2 == "tesoura"):
        print(f"Caso #{case}: Bazinga!")
    elif(p2 == "tesoura" and p1 == "papel"
    or p2 == "papel" and p1 == "pedra"
    or p2 == "pedra" and p1 == "lagarto"
    or p2 == "lagarto" and p1 == "Spock"
    or p2 =="Spock" and p1 == "tesoura"
    or p2 == "tesoura" and p1 == "lagarto"
    or p2 == "lagarto" and p1 == "papel"
    or p2 == "papel" and p1 == "Spock"
    or p2 == "Spock" and p1 == "pedra"
    or p2 == "pedra" and p1 == "tesoura"):
        print(f"Caso #{case}: Raj trapaceou!")
    else:
        print(f"Caso #{case}: De novo!")


def main():
    cases: int = int(input())
    for i in range(1,cases+1):
        p1, p2 = input().split(" ")
        game_rules(i,p1,p2)



if __name__ == "__main__":
    main()