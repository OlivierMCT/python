def calculerCarre(nombre: int) -> int:
  leCarre = nombre ** 2
  #leCarre = nombre * nombre
  return leCarre

def additionner(nb1: int, nb2: int, nb3: int = 0) -> int:
  return nb1 + nb2 + nb3

def soustraire(nb1: int, nb2: int, nb3: int = None) -> int:
  difference = nb1 - nb2
  if(nb3 != None):
    difference -= nb3
  return difference


def multiplier(nb1: int, nb2: int, *nbs: int) -> int:
  produit = nb1 * nb2  
  for nb in nbs:
    produit *= nb
  return produit

def diviser(nb1: int, nb2: int):
  qt = nb1 / nb2
  pe = nb1 // nb2
  r = nb1 % nb2
  return qt, pe, r
  #return (qt, pe, r)

def calculerFactorielle(nb: int) -> int:
  return 1 if(nb == 1) else nb * calculerFactorielle(nb - 1)
  
# def calculerFactorielleBis(nb: int) -> int:
#   facto = 1
#   for i in range(1, nb):
#     facto *= i+1
#   return facto

def calculerFactorielleBis(nb: int) -> int:
  facto = 1
  while(nb > 1):
    facto *= nb
    nb -= 1
  return facto