def fibonacci(n):
    fibonacci_sequence = [0, 1]

    while fibonacci_sequence[-1] <= n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence

while True:
    try:
        numero = int(input("Digite um número positivo: "))
        if numero <= 0:
            raise ValueError
        break
    except ValueError:
        print("Entrada inválida. Digite um número positivo.")

sequencia = fibonacci(numero)

print("Sequência Fibonacci até o primeiro número superior a", numero, ":")
for numero in sequencia:
    print(numero)
