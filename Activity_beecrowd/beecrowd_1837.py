from typing import Any


def starts_numbers() -> tuple[int, int] | None:
    """
    entry numbers
    :return: a and b
    """
    try:
        a,b = (input().split(" "))
        a: int = int(a)
        b: int = int(b)
        return a,b
    except ValueError as error:
        print(error)
    except:
        print("error")

def equation(a: int, b: int):
    """
    Result equation
    :param a: value of a
    :param b: value of b
    :return: nothing
    """
    q = a // b
    r = a % b

    if r < 0:
        q += 1 if b < 0 else -1
        r = a - b * q
    print(f"{q} {r}")

def main():
    a,b = starts_numbers()
    equation(a,b)



if __name__ == "__main__":
    main()