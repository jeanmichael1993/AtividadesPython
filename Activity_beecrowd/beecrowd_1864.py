"""
What's up? Did you enjoy this year's Winter School? For this School to happen, there were many who worked,
whether in the elaboration of the problems, in the configuration of the Portal, in the logistics of the event or in the
fundraising. Our special thanks this year go to Prof. Ricardo Oliveira, who not only agreed to come and teach the workshops
but also actively participated in the organization of the school. We are sure that his experience and career at the ICPC
as a competitor and as a coach motivated and inspired all of us.

We hope you've enjoyed these last few days in Essos and Westeros, that you've learned a lot, and that you've had fun.
But it's not just in Essos and Westeros that you should have fun. Here, in Beyond the Wall, programming is also fun.
Keep studying, keep training, and more and more. The important thing is the path you will take from now on. Our advice
is that you always try to make the most of every moment, every workshop, every school, every workout, every practice or
study time at home. Our days will never return.

Input()
The entry consists of a single integer number N on a line

Output()
Print the first N characters of the quote by Soren Kierkegaard defined by the letters that were underlined in the statement
of this problem. Pay attention, as no spaces were underlined - you must guess the number and location of the spaces in the
sentence. The only line of output should consist only of uppercase letters and spaces and be terminated by a newline.



"""


def main():
    n: int = int(input())
    frase: str = "Life is not a problem to be solved, but a reality to be experienced."
    new_frase: str = frase[:n]
    print(new_frase.upper())


if __name__ == "__main__":
    main()