"""
Three friends played the lottery. If they win, the prize must be divided proportionally to
the amount each gave to make the bet. Make a program that reads how much each player has invested,
 the value of the prize, and prints out how much each player would earn from the prize based on the amount invested.
"""

first_person: float = float(input("Write how much the first player has invested: "))
second_person: float = float(input("Write how much the second player has invested: "))
third_person: float = float(input("Write how much the third player has invested: "))
value_prize: float = float(input("Write how much is value prize: "))
value_total_person: float = first_person + second_person + third_person
percent_first: float = first_person / value_total_person
percent_second: float = second_person / value_total_person
percent_third: float = third_person / value_total_person
print(f"Value prize first winner: {(value_prize * percent_first):.2f}")
print(f"Value prize second winner: {(value_prize * percent_second):.2f}")
print(f"Value prize third winner: {(value_prize * percent_third):.2f}")
