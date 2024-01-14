def validador(numero: int) -> int:
  if numero > 0:
    return 1
  elif numero < 0:
    return -1
  else:
    return 0


if __name__ == "__main__":
  numero: int = int(input("Digite um número: "))
  print(validador(numero))

