def mdc(x,y):
  '''
  int int => int
  mdc(x,y) => z

  Find the greatest common divisor among x and y.
  '''

  a = max(x,y)
  b = min(x,y)
  if (a%b == 0):
      return b
  else:
    for i in reversed(range(1,b)):
      if ((b%i == 0) and (a%i == 0)):
        return i
    return "Não existe mdc"

print(mdc(35,15))
