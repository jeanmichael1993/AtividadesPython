"""
Read an uppercase character, which indicates an operation to be performed and a matrix.
Then, calculate and display the sum or average considering only the elements below the main diagonal of the matrix,
as illustrated below (green area).

Input.
The first line of input contains a single uppercase character O ("S" or "M"),
indicating the operation (Sum or Average) to be performed on the elements of the matrix.
The next lines contain the 144 floating-point values that make up the matrix.

Output:
Print the requested result required (sum or average), with one digit after the decimal point.

"""


def create_matrix(line: int, column: int) -> list:
    matrix: list = [[float(input()) for i in range(line)] for j in range(column)]
    return matrix


def chosen_operation(operation: str, matrix: list, line: int, column):
    if operation == "S":
        __sum__: float = 0
        for i in range(1, line):
            for j in range(i):
                __sum__ += matrix[i][j]
        print(f"{__sum__:.1f}")
    elif operation == "M":
        sum_list: float = []
        for i in range(1, line):
            for j in range(i):
                sum_list.append(matrix[i][j])
        __average__: float = sum(sum_list) / len(sum_list)
        print(f"{__average__:.1f}")


def main():
    line: int = 12
    column: int = 12
    operation: str = input()
    chosen_operation(operation, create_matrix(line, column), line, column)


if __name__ == "__main__":
    main()

