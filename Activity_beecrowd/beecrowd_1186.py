"""
Read an uppercase character, which indicates an operation to be performed and a matrix[12][12].
Then, calculate and display the sum and the average considering only those elements below the second diagonal of the
matrix.

Input()
The first line of input contains a single uppercase character ( "S","M"), indicating an operation (SUM or AVERAGE),
to be performed on the elements of the matrix.

Output()
Print the requested result (sum or average), with one digit after the decimal point.

"""


def create_matrix(lines: int, columns: int) -> list:
    return [[float(input()) for line in range(lines)] for column in range(columns)]


def operation_matrix(lines: int, columns: int, matrix: list, operation: str):

    __list__: list = []
    __sum__: float = 0
    for line in range(1, lines):
        for column in range(columns-line, columns):
            __sum__ += matrix[line][column]
            __list__.append(matrix[line][column])
    if operation == "S":
        print(f"{__sum__:.1f}")
    elif operation == "M":
        __average__: float = __sum__ / len(__list__)
        print(f"{__average__:.1f}")


def main():
    lines = columns = 12
    operation: str = input()
    matrix: list = create_matrix(lines, columns)
    operation_matrix(lines, columns, matrix, operation)

    return None


if __name__ == "__main__":
    main()