import math
class fracao:
  def __init__(self, valorX, valorY):
    self.__x = valorX
    self.__y = valorY

  def setX(self, valor):
    self.__x = valor

  def setY(self, valor):
    self.__y = valor

  def getX(self):
    return self.__x

  def getY(self):
    return self.__y

  def __str__(self):
    return (f'{self.__x,self.__y}')

  def __add__(self, nf):
    return simplifica(fracao(self.__x * nf.__y + self.__x * nf.__y, self.__y * nf.__y))

  def __sub__(self, nf):
    return simplifica(fracao(self.__x * nf.__y - self.__y * nf.__x, self.__y * nf.__y))

  def __mul__(self, nf):
    return simplifica(fracao(self.__x * nf.__x,self.__y * nf.__y))

  def __truediv__(self, nf):
    return simplifica(fracao(self.__x * nf.__y, self.__y * nf.__x))

def simplifica(p3):
  valor = math.gcd(p3.getX(), p3.getY())
  return fracao(p3.getX()/valor, p3.getY()/valor)


if __name__ == '__main__':
  p1 = fracao(5,6)
  p2 = fracao(9,3)
  print(f'{p1} * {p2} == {p1 * p2}')
  print(f'{p1} + {p2} == {p1 + p2}')
  print(f'{p1} - {p2} == {p1 - p2}')
  print(f'{p1} / {p2} == {p1 / p2}')
