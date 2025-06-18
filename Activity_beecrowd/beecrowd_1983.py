
def main():
    amount: int = int(input())
    dict = {}
    for _ in range(amount):
        matricula, nota = input().split()
        matricula:int  = int(matricula)
        nota: float = float(nota)
        dict.update({matricula : nota})

    if max(dict.values()) >= 8:
        print(max(dict, key=dict.get))
    else:
        print("Minimum note not reached")



if __name__ == "__main__":
    main()