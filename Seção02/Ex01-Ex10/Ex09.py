"""
Read the salary of a employee and the value of the installment of a loan, If the installment is greater than 20% of the
salary print: Loan not granted, otherwise print: Loan granted.
"""

salary_of_a_employee: float = float(input("Write the salary of a employee: "))
value_installment: float = float(input("Write the value of the instalment of a loan: "))
twenty_percentage: float = salary_of_a_employee * 0.20
if twenty_percentage > value_installment:
    print("Loan Granted!")
else:
    print("Loan not granted!")



