"""
You have two circular power cables in yours hands. The first cable has radius R1 and the second radius R2.
You need to buy a circular conduit in order to pass the two cables through it:
What is the smallest radius of conduit you should buy? In other words, given two circles, what is the radius of the smallest
circle that can encompass both two?

Input()
In the first row we will have an integer T, indicating the number os test cases.

In the single row of each case we will have two numbers integers R1 and R2, indicating the respective radii.
The integers will be positive, and all the accounts will fit into a normal 32-bit integer.


Output
In each case, print the smallest radius possible on a single row.
"""

def main():
    cases_tests: int = int(input())
    for _ in range(cases_tests):
        r1, r2 = input().split(" ")
        r1: int = int(r1)
        r2: int = int(r2)
        print(r1+r2)


if __name__ == "__main__":
    main()