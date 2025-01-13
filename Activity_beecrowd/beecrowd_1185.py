"""
Read an uppercase character, which indicates an operation to be performed and a matrix M[12][12].
Then, calculate and display the sum and average considering only those elements under the secondary diagonal of matrix.


Input
The first line of input contains a single uppercase character ("S","M"), indicating the operation (Sum and Average),
to be performed on the elements of the matrix.
The next lines contain the 144 floating-point values that make up the matrix.

Output:
Print the requested result required (sum or average), with one digit after the decimal point.

"""


def create_matrix(lines: int, columns: int) -> list:
    """
    Creating matrix.
    :return: matrix
    """
    return [[float(input()) for line in range(lines)] for column in range(columns)]


def operation_matrix(matrix: list, operation: str, lines: int, columns: int):
    """
    Make the operation S or M
    :param matrix: Matrix list
    :param operation: S or M
    :param lines: lines matrix
    :param columns: columns matrix
    :return: None
    """
    __sum__: float = 0
    __list__: list = []
    for line in range(lines - 1):
        for column in range((columns - 1)-line):
            __sum__ += matrix[line][column]
            __list__.append(matrix[line][column])
    if operation == "S":
        print(f'{__sum__:.1f}')
    elif operation == "M":
        __average__: float = __sum__ / (len(__list__))
        print(f'{__average__:.1f}')

def main():
    lines = columns = 12
    operation: str = input()
    matrix: list = create_matrix(lines, columns)
    operation_matrix(matrix, operation, lines, columns)


if __name__ == "__main__":
    main()


