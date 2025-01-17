"""
Read an uppercase character, that indicates an operation to be performed and a matrix[12][12].
Then calculate and display the sum and the average considering only those elements that are upper area of the matrix.

Input()
The first line of input contains a single uppercase character ("S","M"), indicates an operation (SUM or AVERAGE)
to be performed on the elements of matrix.

Output()
Print the requested result (sum or average) with one digit after the decimal point.

"""

def create_matrix(lines: int, columns: int) -> list:
    return [[float(input()) for line in range(lines)] for column in range(columns)]


def operation_matrix(lines: int, columns: int, operation: str, matrix: list):
    __sum__: float = 0
    __list__: list = []

    for line in range(5):
        for column in range(line + 1, (columns -1) - line):
            __sum__ += matrix[line][column]
            __list__.append(matrix[line][column])

    if operation == "S":
        print(f"{__sum__:.1f}")
    elif operation == "M":
        print(f"{(__sum__ / len(__list__)):.1f}")


def main():
    lines = columns = 12
    operation = input()
    operation_matrix(lines,columns,operation,create_matrix(lines,columns))


if __name__ == "__main__":
    main()