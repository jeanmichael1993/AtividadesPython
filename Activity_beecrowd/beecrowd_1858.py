"""
Ramsay."(...) you win if you can guess who I am and why I'm torturing you."
Theon must think fast and guess who his tormentor is! However, Ramsay has already decided what he will do after
Theon gives his answer.

Theon can say that his tormentor is one of N people. Consider that people are numbered from 1 to N. If Theon replies
that his tormentor is person I, Ramsay will hit him Ti times.

Your task is to help Theon determine what his response should be in order to minimize the number of times he will bet hit

Input()
The first row contents an integer N, The second row contents N integers T1,T2...

Output()
print a row containing the number of person that Theon should say is your tormentor. If there is more than one possible
answer, print the smaller one.

"""

def main():
    n: int = int(input())
    people: list = input().split(" ")
    print(people.index(min(people))+1)




if __name__ == "__main__":
    main()