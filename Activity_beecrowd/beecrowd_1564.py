"""
Brazil is the host country of the cup this year. However, there are many people protesting against the government. On social
networks it is possible to see people stating that there will be no cup due to the protests.

But these rumors that there will be no World Cup are totally false, President Dilma Roussef has already warned:
there will be a World Cup, and if you complain there will be two!

Input()
The input contains several test cases and ends whit EOF. Each test case consists of a line containing the number N of complaints
about the cup forwarded to the president.

Output
For each test, the output consists of a line saying "there will be a cup!" if there are no complaints to the president.
If there are complaints, the exit should say "there will be two"!.

"""
import sys


def main():
    try:
        for row in sys.stdin:
            n = int(row.strip())
            if n == 0:
                print("vai ter copa!")
            elif n > 0:
                print("vai ter duas!")
    except EOFError:
        pass



if __name__ == "__main__":
    main()