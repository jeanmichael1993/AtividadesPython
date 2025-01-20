"""
Write an algorithm that read an integer N, correspond the order of a matrix M of integer, and create the matrix
of accord with example

Input()
the input consist of several integers, a value by line, corresponds the orders of matrix to be created. The end of the entry
is marked by an order value of zero.


Output()
For each integer of entry, print the correspond matrix, of accord with the example. The values of matrix must be formatted in
a size field 3 justified on the right and separated by space. After the last character of each row of the matrix
there should be no blank spaces. After the printing each matrix a blank line should be left.

"""

def main():
    x: int = int(input())
    while x != 0:
        __list__: list = [[ (abs(j-i) + 1) for i in range(x)] for j in range(x)]
        for line in __list__:
            print(" ".join(f"{num:3}" for num in line))
        print()
        x = int(input())

if __name__ == "__main__":
    main()