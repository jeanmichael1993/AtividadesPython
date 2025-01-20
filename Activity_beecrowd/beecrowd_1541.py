"""
Mr. PI is a builder very famous at a Programolândia city. He needs your help to find the bests places of city.
for to build  his several  houses' projects.

Consider that he has for example, a project to building a house of 8 meters by 10 meters, and the municipality's legislation
allows the construction of a maximum of 100% of the land. Since all the plots in this city are perfectly square and the value of the sides
of the house are only a reference for the total area to be built (80 square meters), Mr. PI would need a plot of 8,994 meters, which simplified
would give as a result 8 meters and the actual size of the house would be 64 square meters. If the legislation allowed 50% of the land to be used,
it would have to be 160 meters for 50% of it to be 80 square meters, enough for a house of 8 x 8 meters (64 square meters). In the first test case,
as the percentage to build is only 20%, the land would have to be 20 meters on a side so that 1/5 of this land would have the size of 80 square meters.
Help Mr. PI determine the minimum size of the land.

Input()
The entry is compost of several test cases. Each case of test is compost of three integer numbers A,B and C, separated for space.
These numbers represent the measurements of the house (A and B) and the maximum percentage allowed to build in that neighborhood (C).
A single value of 0 indicates the end of entries.

Output()
you must enter a whole number, which represents the measurement of the side of the land. This value should be truncated if necessary.


"""
import math

def main():
    while True:
        entry: str = input().strip()
        if entry == "0":
            break
        a,b,c = map(int, entry.split())
        area_house = a * b
        minimum_land_area = area_house / ( c / 100)
        land_side = math.sqrt(minimum_land_area)
        land_side_truncated = math.trunc(land_side)
        print(land_side_truncated)



if __name__ == "__main__":
    main()
