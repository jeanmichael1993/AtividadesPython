"""
Write an algorithm that read an integer N, corresponding the order of the matrix M of integers, create a matrix of accord
with the example below

Input()
The input consist a lot of integers, one value for line, corresponding the orders of matrix to be created. The end of input
is a valor of order equal to zero.

Output()
For each integer of input print the corresponding matrix, of accord with the example, The values of matrix must be formatted
in a camp of size 3, justified on the right and separated by space, After the last character of each row of the matrix
there should be no blank spaces. After the printing each matrix a blank line should be left.

"""


def main():
    try:
        x: int = int(input())
        while x != 0:
            lines = columns = x
            __list__: list = [[min(line + 1, column + 1, x - line, x - column) for column in range(columns)] for line in range(lines)]
            for linha in __list__:
                print(" ".join(f"{num:3}" for num in linha))
            print()
            x = int(input())
    except ValueError as error:
        print(error)

if __name__ == "__main__":
    main()