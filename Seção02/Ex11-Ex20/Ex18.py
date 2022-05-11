

option_mat: str = input("Write the option mathematics(sum,div,sub,multi) : ")
value_first: float = float(input("Write first value: "))
value_second: float = float(input("Write second value: "))
if option_mat == 'sum':
    print(value_first + value_second)
elif option_mat == 'div':
    print(value_first / value_second)
elif option_mat == 'sub':
    print(value_first - value_second)
elif option_mat == 'multi':
    print(value_first * value_second)
else:
    print("Option Invalid!")
