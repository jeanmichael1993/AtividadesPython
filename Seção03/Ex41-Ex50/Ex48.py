def fibonacci_sum_even(limit):
    sum_even = 0
    fibonacci_sequence = [0, 1]

    while fibonacci_sequence[-1] <= limit:
        if fibonacci_sequence[-1] % 2 == 0:
            sum_even += fibonacci_sequence[-1]

        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return sum_even

limit = 4000000
result = fibonacci_sum_even(limit)
print("A soma dos termos de valor par da sequência de Fibonacci até", limit, "é:", result)
