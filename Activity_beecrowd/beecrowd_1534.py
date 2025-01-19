"""
Read a value integer N that is the size of matrix must be print according to model supplied.

Input()
The entry contains a several cases of test and finish with EOF. Each case of test is compound by a single integer N
, that determines the size (rows and columns) of a matrix that should be printed.

Output

For each N read, present the output as the example provided.

"""
import sys
import math

def create_matrix(N):
    matrix = []
    for i in range(N):
        row = []
        for j in range(N):
            if i == j:
                if N % 2 == 0:
                    row.append(1)  # Diagonal principal
                elif N % 2 != 0:
                    if i == math.floor(N/2) and j == math.floor(N/2):
                        row.append(2)
                    else:
                        row.append(1)
            elif i + j == N - 1:
                row.append(2)  # Diagonal secundária
            else:
                row.append(3)  # Demais posições
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print("".join(map(str, row)))


def main():
    try:
        for row in sys.stdin:
            N = int(row.strip())
            matrix = create_matrix(N)
            print_matrix(matrix)
    except EOFError:
        pass



if __name__ == "__main__":
    main()