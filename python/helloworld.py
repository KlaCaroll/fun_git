def calcul(y: int):
  square : int
  square = y*y
  return(square)
  
def helloworld(x: int):
  # just for fun
  square = calcul(x)
  
  print(f'you\'ll x{square} your level in git ... have you done something ?')

  print('hello world')

helloworld(1)