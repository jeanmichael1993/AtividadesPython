"""
Slug racing is a sport that has grown a lot in recent year, causing many people to dedicate their lives trying to catch
fast slugs, and train them to earn millions in races around the world.
However, the task of capturing fast slugs is not a very easy task, as practically all slugs are very slow. Each slug
is classified into a level depending on its speed:

Level 1 : if the speed is less than 10 cm/h.
level 2 : if the speed is greater than or equal to 10 cm/h and less than 20 cm/h.
level 3 : if the speed is greater than or equal to 20 cm/h.

Your task is to identify which slug's speed level is the fastest in a group of slugs.

Input
The input consists of multiple test cases, and each consists of two lines : the fist line contains an integer L
representing the number of slugs in the group, and the second line contains L integers VI representing the velocities
of each slug in the group.

The entry ends with the end of file (EOF)


Output
For each test case, print a single line indicating the speed level of the fastest slug in the group

"""
from operator import contains


def main():
    try:
        while True:
            l: int = int(input())
            a: list = [(input().split(" "))]
            slugs_list: list =[]
            for i in a:
                for x in i:
                    slugs_list.append(int(x))
            if max(slugs_list) >= 20:
                print("3")
            elif 10 <= max(slugs_list) <= 20:
                print(2)
            else:
                print(1)
    except EOFError as error:
        return None


if __name__ == "__main__":
    main()