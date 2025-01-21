"""
Write an algorthm that read an integer N, correspond an order of a matrix of integers, and build the matrix
of accord by example

Input()
The entry consist of several integers, a value by row, correspond the orders of matrix to be creates. The end of entry
é marked by a value of order equals the zero

Output
For each integer of entry print the matrix correspond, of accord with the example. The values of matrix must be
formatted in a right-justified T-size field and separated by space, where T is equal to the number of digits of the
largest number in the array. After the last character of each row of the array there should be no blank spaces. After
printing each matrix, a blank line should be left.
"""

def main():
    while True:
        n: int = int(input())
        if n == 0:
            break
        matrix = [[2 ** abs(i+j) for j in range(n)] for i in range(n)]

        max_value = matrix[n - 1][n - 1]
        T = len(str(max_value))

        for linha in matrix:
            print(" ".join(f"{x:>{T}}" for x in linha))
        print()
if __name__ == "__main__":
    main()