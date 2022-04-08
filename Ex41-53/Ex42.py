"""
Receive an employee's base salary. Calculate and print the salary to be received,
knowing that this employee has a 5% bonus on the base salary.
in addition, he pays 7% tax on his base salary.
"""

employee_base_salary: float = float(input("Write the employee's base salary: "))
bonus: float = (employee_base_salary * 0.05)
discount: float = (employee_base_salary * 0.07)
net_salary: float = (employee_base_salary - discount) + bonus
print(f"Salary to be received: {net_salary:.2f}")