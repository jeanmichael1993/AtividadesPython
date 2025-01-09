import statistics


def create_array() -> list:
    return [[float(input()) for i in range(12)] for j in range(12)]


def chosen_operation(column: int, operation: str, array: list) -> float:
    if operation == 'S':
        __sum__: float = sum([line[column] for line in array])
        return __sum__
    elif operation == 'M':
        __average__: float = statistics.mean([line[column] for line in array])
        return __average__


def main():
    column: int = int(input())
    operation: str = input()
    array: list = create_array()
    result: float = chosen_operation(column, operation, array)
    print(f"{result:.1f}")


if __name__ == "__main__":
    main()

