"""
Read a value of salary employee. Calculate and print the value of new salary, given that he received a increase of 25%

"""
increase: float = 0.25
salary_employee: float = float(input("Write the value of salary employee: "))
print(f"The new salary is: {(salary_employee + (salary_employee * increase)):.2f}")
