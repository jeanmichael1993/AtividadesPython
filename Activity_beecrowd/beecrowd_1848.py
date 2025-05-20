
def result(text: str, soma: int, rule: dict) -> int:
    soma += rule[text]
    return soma

def rules(rule):
    text = input()
    soma: int = 0
    while text != "caw caw":
        soma = result(text, soma, rule)
        text = input()
    print(soma)

def main():
    rule: dict = {"--*":1, "*--":4, "**-":6, "***":7, "-**":3, "-*-":2, "*-*":5}
    [rules(rule) for i in range(3)]


if __name__ == "__main__":
    main()