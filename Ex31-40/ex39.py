"""
The importance of R$ 780.000,00, is divided in between three winners of a contest.
given that of total amount.

First winner will receive 46%
Second winner will receive 32%
Third winner wil receive remainder.

Calculate and print the amount win for each winner.
"""

value_win: float = 780_000.000
print(f"Value first winner: R${(value_win * 0.46):,.2f} \n Value of second winner: R$"
      f"{(value_win * 0.32):,.2f} \n Value of third winner: R$"
      f"{(value_win - ((value_win * 0.46) + (value_win * 0.32))):,.2f}")

