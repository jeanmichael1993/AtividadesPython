def calcular_consumo(distancia: float, litros: float) -> float:
  """
  Função calcula quantidade de consumo por distance e litros
  :param distancia = distancia pecorrida
  :param litros = quantidade de litros gasta
  :return = valor de distancia por litro
  """
  return distancia/litros

def mostra_resultado(consumo: float) -> str:
  """
  Função que mostra o resultado do consumo do carro!
  :param consumo = valor gasto total
  :return: texto com resposta
  """
  if consumo < 8:
    return "Venda o carro!"
  elif 8 <= consumo <= 12:
    return "Econômico!"
  else:
    return "Super econômico!"


if __name__ == "__main__":
  distancia: float = float(input("Digite a distância em KM: "))
  litros: float = float(input("Digite a quantidade de litros de gasolina consumidos: "))
  consumo: float = mostra_resultado(calcular_consumo(distancia, litros))
  print(consumo)
